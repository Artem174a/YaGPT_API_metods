# YaGPT API

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

This Python library provides a simple wrapper for interacting with Yandex Language Models, making it easy to send requests for text generation.

## Features
**Simplified Interaction:** Easily send requests to Yandex Language Models with just a few lines of code.

**Error Handling:** Robust error handling for HTTP requests and unexpected errors.

**Example Usage:** Included example for quick integration into your projects.

## Installation

```bash
pip install YaGPT
```

## Usage
```python
from YaGPT import YaGPT, YaGPTException

# Replace with your actual values
folder_id = "your_folder_id"
iam_token = "your_iam_token"

# Create a LanguageModel instance
lm = YaGPT(folder_id, iam_token)

try:
    # Send a request to the language model
    result = lm.instruct(
            model="general",
            instruction_text="Найди ошибки в тексте и исправь их",
            request_text="Ламинат подойдет для укладке на кухне или в детской комнате",
            max_tokens=1500,
            temperature=0.6)

    if result:
        for alternative in result:
            print(f"Generated Text: {alternative['text']}")
            print(f"Score: {alternative['score']}")
            print(f"Number of Tokens: {alternative['num_tokens']}")
            print()
except YaGPTException as e:
    print(f"Language Model Error: {e}")
```