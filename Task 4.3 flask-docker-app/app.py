from flask import Flask, jsonify
import datetime

app = Flask(__name__)

# Route 1: Home Page
@app.route('/')
def home():
    return """
    <html>
        <head><title>Task 4.3 Flask App</title></head>
        <body style="font-family: Arial; padding: 30px; background-color: #f4f4f9;">
            <h1 style="color: #2c3e50;">Hello from Flask Docker Web App! 🚀</h1>
            <p><strong>Task 4.3 Distinction Achieved</strong></p>
            <hr>
            <h3>Explore other endpoints:</h3>
            <ul>
                <li><a href="/about">About Page</a></li>
                <li><a href="/status">System Status (JSON)</a></li>
            </ul>
        </body>
    </html>
    """

# Route 2: About Page
@app.route('/about')
def about():
    return """
    <html>
        <head><title>About - Task 4.3</title></head>
        <body style="font-family: Arial; padding: 30px;">
            <h1>About This Application</h1>
            <p>This is a custom multi-route Flask web application containerized using Docker for unit SWE40006.</p>
            <a href="/">⬅ Back to Home</a>
        </body>
    </html>
    """

# Route 3: JSON Status Page (Great for API testing evidence)
@app.route('/status')
def status():
    return jsonify({
        "status": "healthy",
        "container": "running",
        "timestamp": str(datetime.datetime.now()),
        "unit": "SWE40006"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)