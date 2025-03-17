''' Executing this function initiates the application of emotion 
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. 
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if not response['dominant_emotion'] is None:
        dct = ', '.join([
            f"'{i}': {j}" for i,j in response.items() 
            if i not in ('dominant_emotion', 'sadness')
            ])+f" and 'sadness': {response['sadness']}"+'.'
        sent1 = "For the given statement, the system response is "+dct
        sent2 = f" The dominant emotion is {response['dominant_emotion']}."
        return sent1+sent2
    return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host='0.0.0.0', port=5000)
