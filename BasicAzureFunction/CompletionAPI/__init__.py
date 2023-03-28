import logging
import openai
import azure.functions as func

secret_key = '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'

# Below is the sample request
# {"model":"text-davinci-003","prompt":"Tell me a slogan for indian independence day","max_tokens":150,"temperature":0}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    openai.api_key = secret_key

    req_body = req.get_json()

    output = openai.Completion.create(
        model=req_body['model'],
        prompt=req_body['prompt'],
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature']
    )

    output_text = output.choices[0].text

    return func.HttpResponse(output_text, status_code=200)