# Lab Work 8 – Azure Function OpenAI Façade

This repository contains the source code for Lab Work 8.

The project implements an HTTP-triggered Azure Function in Python that acts as a façade for an OpenAI language model.  
The function receives a query via HTTP request, forwards it to OpenAI, and returns the generated response.

The OpenAI API key is stored securely as an environment variable in Azure Application Settings.
