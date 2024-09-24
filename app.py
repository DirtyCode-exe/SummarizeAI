from flask import Flask, render_template, request, send_file
import os
#import torch
from fpdf import FPDF
from transformers import pipeline
import soundfile as sf
from pydub import AudioSegment

app = Flask(__name__)

# Define paths for saving audio files and PDFs
UPLOAD_FOLDER = "uploads"
PDF_FOLDER = "pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PDF_FOLDER, exist_ok=True)

# Load Hugging Face models
transcriber = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-large-960h")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def transcribe_audio(file_path):
    # Convert to WAV format using pydub
    audio = AudioSegment.from_file(file_path)  # Automatically detects format
    audio = audio.set_frame_rate(16000)
    wav_file_path = "uploads/recorded_audio.wav"
    audio.export(wav_file_path, format="wav")

    # Now read the WAV file with soundfile
    audio_input, _ = sf.read(wav_file_path)

    # Transcribe the audio
    transcription = transcriber(audio_input)["text"]

    # Optionally, remove the temporary file
    os.remove(wav_file_path)
    print(transcription)
    return transcription


def summarize_text(text):
    """Summarize text using BART."""
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']


def save_as_pdf(summary, file_name):
    """Save summary as a PDF."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=summary)
    pdf.output(file_name)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        # Save the uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Transcribe the audio
        transcript = transcribe_audio(file_path)
        pdf_file = os.path.join(PDF_FOLDER, 'transcript.pdf')
        save_as_pdf(transcript, pdf_file)
        # Summarize the transcript
        summary = summarize_text(transcript)

        # Save summary as a PDF
        pdf_file = os.path.join(PDF_FOLDER, 'summary.pdf')
        save_as_pdf(summary, pdf_file)

        # Return the PDF file to the user
        return send_file(pdf_file, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
