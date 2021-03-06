# Simple Python RESTful API with Flask

This project provides a simple flask RESTful API interface to read, write and delete to a Tiny DB instance, either by source_id or by log value.

## Requirements
Python3 is required

This project uses TinyDB, Flask, and Flask_restful. It is recommended to use a venv and install there the project dependencies using the following command:

`pip install -r requirements.txt`

## Usage:

- Display all DB entries

`curl --location --request GET 'http://localhost:5000'`

- Create a new SOURCE_ID entry with json object log value VALUE

`curl --location --request POST '127.0.0.1:5000/source/<SOURCE_ID>' \ 
--header 'Content-Type: application/json' \
--data-raw '{"value":"<VALUE>"'`
  
- Find DB entries by SOURCE_ID

`curl --location --request GET '127.0.0.1:5000/source/<SOURCE_ID>'`

- Find DB entries by log VALUE

`curl --location --request GET '127.0.0.1:5000/logs/<VALUE>'`
  
- Delete DB entries by SOURCE_ID

`curl --location --request DELETE '127.0.0.1:5000/source/<SOURCE_ID>'`

- Delete DB entries by log VALUE

`curl --location --request DELETE '127.0.0.1:5000/logs/<VALUE>'`
  
Each DB entry has the following schema

    {
      "id": <ID_NUMBER>,
      "source": {
          "log": {
              "value": "<VALUE>"
          },
          "source_id": "<SOURCE_ID>",
          "timestamp": <TIMESTAMP>
      }
