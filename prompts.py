# Uses the ChatGPT API to summarize each song in the lyrics.json file, then conjoins each song
# with its summary to create a list of prompts to refine the GPT-3 model with.

import os
import openai
import json
import jsonlines
openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")

with open('lyrics.json') as f:
    data = json.load(f)

prompts = []

# For each song in the lyrics.json file, summarize it and add it to the prompts list
for song in data:
    if song == "" or song == None:
        continue
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant who is an expert on pop culture, and specifically the history of hip hop."},
                {"role": "user", "content": "Please give a one-sentence summary of the following song. Your response should be in the format \"A song titled '<title>' about <description>.\". Here are the lyrics: \n" + song},
            ]
        )
    description = response['choices'][0]['message']['content']
    print(description)
    prompts.append({
        "prompt": description,
        "completion": "\n" + song
        })
    
# Create a JSONL file with the prompts
with jsonlines.open('prompts.jsonl', mode='w') as writer:
    writer.write_all(prompts)