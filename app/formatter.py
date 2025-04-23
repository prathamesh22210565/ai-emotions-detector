def format_result(emotion_data):
    sorted_emotions = sorted(emotion_data.items(), key=lambda x: x[1], reverse=True)
    return {"top_emotion": sorted_emotions[0][0], "scores": sorted_emotions}
