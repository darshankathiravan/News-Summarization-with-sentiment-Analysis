# tts_utils.py
from gtts import gTTS
import tempfile
from translate import Translator  # For translation to Hindi

def generate_tts(text, lang="hi"):
    """
    Translates English text to Hindi, splits it into chunks, generates speech using gTTS,
    and returns the file path.
    """
    if not text.strip():
        return None  # No speech if text is empty

    # Translate the text to Hindi
    try:
        translator = Translator(to_lang=lang)
        translated_text = translator.translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        translated_text = text  # Fallback to original text if translation fails

    # Split the translated text into chunks of 100 characters
    chunk_size = 100  # gTTS free API limit
    chunks = [translated_text[i:i + chunk_size] for i in range(0, len(translated_text), chunk_size)]

    # Generate TTS audio for each chunk and combine them
    tts_audio_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3").name
    with open(tts_audio_path, "wb") as audio_file:
        for chunk in chunks:
            tts = gTTS(chunk, lang=lang)
            tts.write_to_fp(audio_file)

    return tts_audio_path