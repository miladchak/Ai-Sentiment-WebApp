# app.py
from flask import Flask, request, jsonify, send_from_directory
import os
from transformers import pipeline

app = Flask(__name__, static_folder='../frontend', static_url_path='') # Absolute path for static folder

# Load sentiment analysis pipeline - Run once during app startup
try:
    sentiment_analyzer = pipeline("sentiment-analysis") # Default English model (best default)
    print("DEBUG: AI Sentiment Analysis Model (English default) loaded successfully.")
except Exception as e:
    print(f"DEBUG: Error loading AI Sentiment Analysis Model (English default): {e}")
    sentiment_analyzer = None # Set to None if model fails to load


def analyze_sentiment_ai(text):
    """
    Analyzes text sentiment using pre-trained Hugging Face Transformers model (English default).
    Utilizes AI model only and returns detailed sentiment labels.
    """
    print(f"DEBUG: Analyzing sentiment with AI Model (English default) for text: '{text}'") # Debug message

    if sentiment_analyzer is None: # Check if model loaded successfully
        print("DEBUG: AI Model (English default) not loaded. Error in AI Analysis.") # Clearer error message
        return "Error in AI Analysis" # Return error message if model failed

    try:
        result = sentiment_analyzer(text) # Use model for sentiment analysis
        label = result[0]['label'] # Get sentiment label (detailed classification)

        sentiment = label # Return model's label directly (detailed sentiment)

        print(f"DEBUG: AI Sentiment Analysis Result (English default): '{sentiment}' (Model Label: '{label}')") # Debug output with label
        return sentiment # Return detailed sentiment label

    except Exception as e: # Error handling for AI model issues
        print(f"DEBUG: Error during AI Sentiment Analysis (English default): {e}")
        return "Error in AI Analysis" # Return error message

@app.route('/analyze_sentiment', methods=['POST'])
def analyze():
    """
    Endpoint to receive text from frontend and return sentiment analysis result.
    Uses analyze_sentiment_ai function (English default model).
    """
    print("DEBUG: Request received at '/analyze_sentiment' endpoint.") # Debug log for endpoint hit

    try:
        data = request.get_json() # Get JSON data from request
        text = data.get('text') # Extract text from JSON data

        if not text:
            print("DEBUG: Input text was empty.") # Debug log for empty text
            return jsonify({'error': 'Input text is required.'}), 400 # Return 400 error for missing text

        print(f"DEBUG: Text received from frontend: '{text}'") # Debug log for received text

        sentiment = analyze_sentiment_ai(text) # Call AI sentiment analysis function

        return jsonify({'sentiment': sentiment}), 200 # Return sentiment analysis result with 200 OK

    except Exception as e:
        print(f"DEBUG: Unexpected error in analyze function: {e}") # Debug log for unexpected errors
        print(f"DEBUG: Error Type: {type(e)}") # Debug log for error type
        print(f"DEBUG: Error Details: {e}") # Debug log for error details
        return jsonify({'error': 'Error processing sentiment analysis request.'}), 500 # Return 500 error for server-side issues

@app.route('/') # Route for root URL to serve index.html
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) # Run Flask app in debug mode, accessible externally