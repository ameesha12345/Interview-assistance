# Interview-assistance
# Interview Assistant AI - Setup Instructions

## Prerequisites
- Python 3.7+ installed
- Groq API key (sign up at https://console.groq.com/)

## Setup Steps

1. **Create project directory**
   ```bash
   mkdir interview-assistant
   cd interview-assistant
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install flask groq
   ```

5. **Create project structure**
   ```bash
   mkdir templates
   ```

6. **Save the Python script as `app.py`**

7. **Save the HTML file in `templates/index.html`**

8. **Set your Groq API key as an environment variable**
   - Windows: `set GROQ_API_KEY=your_api_key_here`
   - Mac/Linux: `export GROQ_API_KEY=your_api_key_here`

9. **Run the application**
   ```bash
   python app.py
   ```

10. **Open in browser**
    - Navigate to http://127.0.0.1:5000/

## Notes on Customization

- **Model Selection**: The code uses "llama3-70b-8192" but you can change this to any model Groq supports
- **Question Format**: Modify the prompt in the code to change the type of questions generated
- **Styling**: The application uses Bootstrap for styling, which you can customize as needed
- **Error Handling**: Basic error handling is implemented, but you may want to enhance it for production
