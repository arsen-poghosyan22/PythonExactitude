import openai
from config.config import api_key


def generate_docstring(prompt, api_key):
    # Parameters for the generation request
    params = {
        "engine": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 1.0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stop": "\n\n",
    }

    # Call the OpenAI API for text generation
    response = openai.Completion.create(**params, api_key=api_key)

    # Extract the generated text from the response
    generated_text = response.choices[0].text.strip()

    return generated_text

generated_docstring = generate_docstring(prompt, api_key)
