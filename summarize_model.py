from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text, max_chunk_length=1024):
    """Summarize text using BART-Large-CNN, handling both short and long texts."""
    if len(tokenizer.encode(text)) > max_chunk_length:
        # Split the text into chunks of `max_chunk_length`
        chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
        
        # Summarize each chunk
        summaries = [summarize_text(chunk) for chunk in chunks]
        
        # Combine the summaries and return the final summary
        full_summary = " ".join(summaries)
        return summarize_text(full_summary)  # Optionally summarize the combined summary
    else:
        # If text is short, summarize it directly
        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=max_chunk_length, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
