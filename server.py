""" This module hosts the server that runs the emotion detector app."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    """This function returns the output of the emotion detector."""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {response['anger']},"+\
    f" 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']},"+\
    f" and 'sadness': {response['sadness']}. The dominant emotion is"+\
    f" {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """This function renders the html provided."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
