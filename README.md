# AI Content Moderation

Project completed in 2025 – documented here for portfolio purposes.

## 📌 Overview

AI Content Moderation is a Python application designed to help users identify potentially harmful or cyberharassing content in messages.

The user enters a message into the application, and an AI model analyzes it and provides:

- An overall toxicity score
- A risk level
- Detailed scores for different types of harmful content
- The analysis time

The application is intended as an assistance tool for users who want to better understand potentially harmful messages.

## ⚙️ How it works

The application uses the **Detoxify multilingual model** to analyze the submitted text.

The model evaluates several categories of potentially harmful content, including :

- Toxicity
- Insult
- Obscene content
- Identity attack
- Threat
- Sexual explicit content
- Severe toxicity

The application then sorts the detected categories by their scores and determines an overall risk level based on the toxicity score :

- **LOW** : toxicity below 30%
- **MEDIUM** : toxicity between 30% and 70%
- **HIGH** : toxicity at or above 70%

The individual category scores are also displayed so that the user can see which types of harmful content contributed to the result.

## 💻 Technologies

| Category                          | Technology                         |
| ----------------------------------| ---------------------------------- |
| **Programming Language**          | Python 3                           |
| **User Interface (UI)**           | CustomTkinter                      |
| **Toxicity Detection Model**      | Detoxify                           |
| **AI Framework**                  | PyTorch                            |
| **NLP Library**                   | Hugging Face Transformers          |

## ✨ Features

- 📝 Text-based content analysis
- 🌐 Multilingual toxicity detection
- 📊 Detailed category scores
- 🚨 Automatic risk-level classification
- ⏱️ Analysis time measurement
- 🗣️ English and French interface
- 🔄 Reset functionality
- 💡 Example messages for testing

## 📁 Project Structure

```
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
│
├── detector.py
├── interface.py
├── main.py
├── translations.py
└── requirements.txt
```

### 📄 Main Files

**`main.py`**  
Starts the application.

**`interface.py`**  
Contains the graphical interface and handles user interaction.

**`detector.py`**  
Loads the Detoxify model, analyzes the text, calculates the risk level and formats the results.

**`translations.py`**  
Contains the English and French interface translations.

**`requirements.txt`**  
Lists the Python packages required to run the project.

## 🚀 Installation

Clone the repository and install the required dependencies :

```bash
pip install -r requirements.txt
```

Then start the application with :

```bash
python main.py
```

The Detoxify model will be loaded when the application starts.

## 🧪 Testing

The `test_messages` folder contains several example messages that can be copied into the application to test different situations:

- Neutral content
- Friendly content
- Criticism
- Insults
- Harassment
- Severe harassment

These examples allow the user to compare how the model reacts to different levels and types of potentially harmful content.

## ⚠️ Limitations

The application does not determine with certainty whether a person is being cyberharassed.

The percentages are predictions produced by an AI model and should therefore be interpreted as indicators rather than absolute judgments.

Context, irony, personal relationships and other factors may affect how a message should be interpreted.

The application is designed as an analysis and awareness tool rather than a replacement for human judgment.

## 📸 Preview

- **Main interface**
<img width="549" height="778" alt="Screenshot 1" src="https://github.com/user-attachments/assets/89e24e21-de2e-4a9b-bd91-b04617140aa2" />

- **Content analysis**
<img width="578" height="898" alt="Screenshot 2" src="https://github.com/user-attachments/assets/29c9c1a7-d0db-4df0-815e-8c326761d667" />

## 👨‍💻 Author

**Yassine Najeh**

Computer Engineering student interested in embedded systems, Artificial Intelligence and hardware-software integration.
