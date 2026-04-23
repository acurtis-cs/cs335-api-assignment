# CS 335 API Assignment
**Northeastern Illinois University — Introduction to Artificial Intelligence**  

Student: Alex Curtis
API Used: Google Gemini API

---

## Overview

This project uses the Gemini API to make 3 different API calls using Python.

The program runs in the terminal and prints the responses directly to the screen.

The 3 API calls are:

1. What is machine learning?
2. What is supervised learning?
3. User input question for Gemini

The API key is stored safely in the env file and loaded using python-dotenv.

---

## Step-by-Step Setup

### Step 1 — Clone the Course Repo

Clone the full course repository and navigate to this assignment's folder:

```bash
git clone https://github.com/osindy/NEIU335AI.git
cd NEIU335AI/assignments/assignment-01-api
```

### Step 2 — Create a Virtual Environment

A virtual environment isolates this project's dependencies from your system Python.

Used: # Windows (Command Prompt)

Go to the assignment folder

```bash
cd NEIU335AI/assignments/api_assignment
```

Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the start of your prompt — this confirms the environment is active.

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Set Up Your API Key

Copy the example environment file and fill in your real API key:

```bash
copy .env.example .env
```

Open `.env` in any text editor and replace the placeholder:

```
MY_API_KEY=your_actual_api_key_here
```

> **Important:** Never commit your `.env` file. It is covered by the repo's root `.gitignore`.


### Step 5 — Run the Script

```bash
python starter.py
```

You should see formatted output in the terminal for each of the 3 API calls.

### Sample Output

CALL 1

Machine learning enables computers to learn from data without explicit programming.

CALL 2

Supervised learning is a machine learning technique where an algorithm learns from labeled data.

CALL 3

User input:
What day is it today?

Response:
Today is Thursday.

Program finished successfully.
