secret_key = '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'
prompt = 'Tell me a slogan for indian independence day'

import os
import openai
openai.api_key = secret_key

output = openai.Completion.create(
    model='text-davinci-003',
    prompt=prompt,
    max_tokens=150,
    temperature=0
)

output_text = output.choices[0].text

print(output_text)