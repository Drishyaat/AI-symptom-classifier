# AI Symptom Classifier

A Streamlit-powered web app that uses AI to analyze patient-reported symptoms and guide them to the appropriate hospital ward—General, Emergency, or Mental Health.  
This tool aims to improve hospital triage, increase workflow efficiency, and enhance patient experience with clear, instant recommendations.

---

## Features

- User-friendly web interface for entering symptoms
- AI-powered triage and ward classification
- Color-coded, actionable instructions (General, Emergency, Mental Health)
- Customizable favicon for professional appearance
- Efficient, fast deployment via Streamlit

---

## How to Run Locally

1. **Clone this repository:**
    ```
    git clone https://github.com/Drishyaat/AI-symptom-classifier.git
    cd AI-symptom-classifier
    ```

2. **Create and activate a virtual environment (recommended):**
    ```
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3. **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**
    ```
    streamlit run app.py
    ```

---

## Project Structure

.
├── app.py # Main Streamlit app
├── classifier.py # Symptom processing logic
├── favicon.png # Custom site favicon
├── requirements.txt # Python dependencies
├── README.md # Project overview and instructions
└── .gitignore # Git ignore rules


---

## Dependencies

All dependencies are listed in `requirements.txt`.

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

*Created by Drishyaa*
