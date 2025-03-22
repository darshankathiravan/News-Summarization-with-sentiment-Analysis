from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch

# Use the Hugging Face model ID
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Initialize pipeline
device = "cuda" if torch.cuda.is_available() else "cpu"
sentiment_pipe = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0 if device == "cuda" else -1)

def analyze_sentiment(text):
    """Analyzes sentiment of the given text using RoBERTa model."""
    result = sentiment_pipe(text)[0]
    
    # Map numerical labels to sentiment categories
    label_map = {
        "LABEL_0": "Negative",
        "LABEL_1": "Neutral",
        "LABEL_2": "Positive"
    }
    
    sentiment_label = label_map.get(result["label"], "Unknown")
    sentiment_score = result["score"]
    
    return sentiment_label, sentiment_score