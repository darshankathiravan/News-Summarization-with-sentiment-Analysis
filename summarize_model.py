from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text):
    """Summarize text using BART-Large-CNN"""
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    return summary

# Sample text
news_content = """
Tesla's latest electric vehicle has broken sales records in Q3, surpassing expectations. 
With the demand for EVs rising, the company has seen a significant increase in market share, 
despite supply chain challenges. Elon Musk attributes this success to improved battery technology 
and the expansion of Tesla’s Gigafactories.
"""

# Test summarization
summary = summarize_text(news_content)
print("🔹 Original Text:\n", news_content)
print("\n✅ Summary:\n", summary)
