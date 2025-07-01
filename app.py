# app.py
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    """
    Renders the home page of the portfolio.
    """
    # You can pass data to your template here if needed
    portfolio_data = {
        "name": "Your Name",
        "tagline": "Passionate Developer & Innovator",
        "about_me": "Hello! I'm a software developer with a passion for building robust and scalable applications. I specialize in backend development and enjoy solving complex problems with elegant code. When I'm not coding, you can find me exploring new technologies or hiking in the mountains.",
        "projects": [
            {"title": "Project Alpha", "description": "A web application for task management.", "link": "#"},
            {"title": "Project Beta", "description": "A data visualization tool built with Python.", "link": "#"},
            {"title": "Project Gamma", "description": "An e-commerce backend API.", "link": "#"},
        ],
        "contact_email": "your.email@example.com",
        "linkedin_url": "https://linkedin.com/in/yourprofile",
        "github_url": "https://github.com/yourusername"
    }
    return render_template('index.html', data=portfolio_data)

# Run the Flask application
if __name__ == '__main__':
    # When running locally, debug=True allows for auto-reloading and better error messages.
    # For production, set debug=False.
    app.run(host='0.0.0.0', port=5000, debug=True)
