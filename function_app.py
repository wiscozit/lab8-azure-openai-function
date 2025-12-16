import os
import azure.functions as func
from openai import OpenAI

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="ask")
def ask(req: func.HttpRequest) -> func.HttpResponse:
    q = req.params.get("q")

    if not q:
        try:
            body = req.get_json()
            q = body.get("q")
        except Exception:
            q = None

    if not q:
        return func.HttpResponse(
            "Missing parameter. Use ?q=your_question or JSON body {\"q\":\"...\"}",
            status_code=400
        )

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return func.HttpResponse("OPENAI_API_KEY is not set.", status_code=500)

    client = OpenAI(api_key=api_key)

    try:
        resp = client.responses.create(
            model="gpt-5-nano",
            input=q
        )
        return func.HttpResponse(resp.output_text, status_code=200, mimetype="text/plain")
    except Exception as e:
        return func.HttpResponse(f"OpenAI call failed: {e}", status_code=500)
