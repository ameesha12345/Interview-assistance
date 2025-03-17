from flask import Flask, render_template, request, jsonify
import os
from groq import Groq

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_questions', methods=['POST'])
def generate_questions():
    # Get form data
    data = request.form
    full_name = data.get('full_name')
    email = data.get('email')
    phone = data.get('phone')
    experience = data.get('experience')
    position = data.get('position')
    location = data.get('location')
    tech_stack = data.get('tech_stack')
    
    # Create prompt for LLM
    prompt = f"""
    Generate 10 relevant technical interview questions for a candidate with the following profile:
    - Position applying for: {position}
    - Years of experience: {experience}
    - Technical skills: {tech_stack}
    
    The questions should assess both technical knowledge and practical experience.
    Format the response as a JSON array of questions.
    """
    
    # Call Groq API
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",  # Using LLaMA 3 model from Groq
            messages=[
                {"role": "system", "content": "You are an expert technical interviewer for tech positions."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2048,
        )
        
        # Extract questions from response
        questions = response.choices[0].message.content
        return jsonify({"questions": questions})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    if not os.environ.get("GROQ_API_KEY"):
        print("Warning: GROQ_API_KEY environment variable not set")
    app.run(debug=True)