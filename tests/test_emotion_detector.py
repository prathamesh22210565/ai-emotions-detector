from app.emotion_detector import detect_emotion

def test_detect_emotion():
    result = detect_emotion("I am so happy today!")
    assert "joy" in result
