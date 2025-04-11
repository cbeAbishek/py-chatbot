# Web Chatbot

This project implements a simple chatbot with a web user interface. The chatbot is designed to answer user questions based on a predefined knowledge base and allows users to teach it new responses.

## Project Structure

```
web-chatbot
├── backend
│   ├── app.py                # Python code for the chatbot backend
│   ├── knowledge_base.json    # JSON file storing the chatbot's knowledge base
│   └── requirements.txt       # Python dependencies required for the backend
├── frontend
│   ├── index.html            # Main HTML file for the web user interface
│   ├── styles.css            # CSS styles for the web user interface
│   └── app.js                # JavaScript code for handling user interactions
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd web-chatbot
   ```

2. **Install backend dependencies:**
   Navigate to the `backend` directory and install the required Python packages:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the backend:**
   Start the chatbot server by running:
   ```
   python app.py
   ```

4. **Open the frontend:**
   Open `frontend/index.html` in your web browser to access the chatbot interface.

## Usage Guidelines

- Type your question in the input field and press Enter or click the submit button.
- If the chatbot does not know the answer, you can provide a new response to teach it.
- Type "quit" in the input field to exit the chatbot.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are welcome!