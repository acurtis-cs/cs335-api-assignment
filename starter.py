# CS 335 — Introduction to Artificial Intelligence
# API Assignment Starter Code — Northeastern Illinois University
#
# TODO: Replace BASE_URL, endpoints, params, and payload fields
#       with values from your chosen API's documentation.
# ─────────────────────────────────────────────────────────────


import os
import json
import requests
from dotenv import load_dotenv

# load the API key from the .env file
load_dotenv()

API_KEY = os.getenv("MY_API_KEY")

# stop the program if the key is missing
if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

# Geminii base URL
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent"

# headers of API request
HEADERS = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY
}


# makes the output easier to read
def divider(label):
    print("\n" + "=" * 50)
    print(label)
    print("=" * 50)


# Prints the AI text if the request worked
def print_result(data):
    try:
        print(data["candidates"][0]["content"]["parts"][0]["text"])
    except:
        print("Could not read response text.")
        print(json.dumps(data, indent=2))


# Call 1
# asking Gemini a basic question
def call_one_post():
    divider("CALL 1")

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": "What is machine learning? Answer in exactly 2 short sentences."}
                ]
            }
        ]
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        print_result(data)
    else:
        print(f"Error {response.status_code}: {response.text}")


# Call 2
# asingk Gemini to explain a topic in a different way
def call_two_post():
    divider("CALL 2")

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": "What is supervised learning? Answer in exactly 2 short sentences."}
                ]
            }
        ]
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        print_result(data)
    else:
        print(f"Error {response.status_code}: {response.text}")


# Call 3
# User input creats question 
def call_three_parameterized(user_input):
    divider("CALL 3")

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_input + " Answer in exactly 2 short sentences."}
                ]
            }
        ]
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        data = response.json()
        print_result(data)
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    call_one_post()
    call_two_post()

    user_prompt = input("\nEnter your own prompt for Call 3: ")
    call_three_parameterized(user_prompt)

    print("\nProgram finished successfully.")
