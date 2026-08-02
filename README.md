# 🤖 AI Content Moderation

AI-powered application for detecting potentially toxic or cyberharassing content in text.

## 📌 Project Overview

AI Content Moderation is a Python application designed to help users identify potentially harmful or cyberharassing content in messages.

The user enters a message into the application, and an AI model analyzes it and provides:

- An overall toxicity score
- A risk level
- Detailed scores for different types of harmful content
- The analysis time

The application is intended as an assistance tool for users who want to better understand potentially harmful messages.

## ⚙️ How It Works

The application uses the **Detoxify multilingual model** to analyze the submitted text.

The model evaluates several categories of potentially harmful content, including:

- Toxicity
- Insult
- Obscene content
- Identity attack
- Threat
- Sexual explicit content
- Severe toxicity

The application then sorts the detected categories by their scores and determines an overall risk level based on the toxicity score:

- **LOW**: toxicity below 30%
- **MEDIUM**: toxicity between 30% and 70%
- **HIGH**: toxicity at or above 70%

The individual category scores are also displayed so that the user can see which types of harmful content contributed to the result.

## 💻 Technologies

- Python
- CustomTkinter
- Detoxify
- PyTorch
- Hugging Face Transformers

## ✨ Features

- Text-based content analysis
- Multilingual toxicity detection
- Detailed category scores
- Automatic risk-level classification
- Analysis time measurement
- English and French interface
- Reset functionality
- Example messages for testing

## 📂 Project Structure

```text
AI Content Moderation/
│
├── screenshots/
│   ├── Screenshot 1.png
│   └── Screenshot 2.png
│
├── test_messages/
│   ├── 01_neutral.txt
│   ├── 02_friendly.txt
│   ├── 03_criticism.txt
│   ├── 04_insult.txt
│   ├── 05_harassement.txt
│   ├── 06_severe_harassement.txt
│   └── 07_threat.txt
│
├── detector.py
├── interface.py
├── main.py
├── translations.py
└── requirements.txt
