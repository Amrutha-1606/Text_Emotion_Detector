# Text Emotion Detector

# Emotion keywords
emotions = {
    "Happy": [
        "happy",
        "joy",
        "excited",
        "great",
        "wonderful",
        "love"
    ],

    "Sad": [
        "sad",
        "unhappy",
        "cry",
        "lonely",
        "upset",
        "miss"
    ],

    "Angry": [
        "angry",
        "furious",
        "mad",
        "hate",
        "annoyed",
        "irritated"
    ],

    "Fear": [
        "afraid",
        "scared",
        "fear",
        "worried",
        "nervous",
        "danger"
    ]
}

# Get input from user
text = input("Enter a sentence: ").lower()

# Remove punctuation
for symbol in ".,!?;:":
    text = text.replace(symbol, "")

# Convert sentence into words
words = text.split()

# Store emotion scores
scores = {}

# Count matching emotion words
for emotion, keywords in emotions.items():

    score = 0

    for word in words:
        if word in keywords:
            score += 1

    scores[emotion] = score

# Check whether any emotion was detected
if max(scores.values()) == 0:

    print("\nEmotion: Unknown")

else:

    detected_emotion = max(
        scores,
        key=scores.get
    )

    print("\nDetected Emotion:",
          detected_emotion)