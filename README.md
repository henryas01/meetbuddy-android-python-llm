# MeetBuddy

Android + Python backend powered by LLMs.

---

## Overview

MeetBuddy is an AI assistant backend written in Python.
Designed to be consumed by an Android client.
Processes natural language input.
Returns intelligent responses (text, code, utilities).

---

## Tech Stack

- Python
- SQLite
- LLM (pluggable)
- REST-style API
- Android client (external)

---

## Structure
├── main.py # entry point
├── ai/ # LLM logic
├── api/ # API routes
├── utils/ # helpers
├── database/ # DB logic
├── app.db # main database
├── ielts.db # sample database
├── test_tts.py # TTS test
├── requirements.txt
└── README.md

---

## Flow

Android App
↓
API Request
↓
LLM Processing
↓
Response
↓
Android App



---

## Setup

```bash
git clone https://github.com/henryas01/meetbuddy-android-python-llm.git
cd meetbuddy-android-python-llm
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate
pip install -r requirements.txt
python main.py
python test_tts.py
Database

SQLite

Lightweight

Local

Extendable

Notes

Android client not included

LLM provider can be swapped

API can be extended

Suitable for local or cloud deployment

Status

Experimental.
Under development.
