from transformers import pipeline

# Load once at the top level (for performance)
emotion_classifier = pipeline("text-classification", 
                              model="j-hartmann/emotion-english-distilroberta-base", 
                              return_all_scores=True)

def detect_emotion(text):
    scores = emotion_classifier(text)[0]  # List of dicts
    emotion_scores = {item['label'].lower(): item['score'] for item in scores}
    return emotion_scores
