# Audio Transcription and Summarization AI App
<img width="954" alt="msedge_cWgoF8VfzJ" src="https://github.com/user-attachments/assets/4b3d1920-a490-4224-a9a9-d3c5e70ed25c">
<img width="960" alt="chrome_wy1lQs9PbO" src="https://github.com/user-attachments/assets/1655c54e-8e1f-4c8a-8b5e-865c682c9885">
This Flask-based web application allows users to record live audio from their browser, transcribe the recorded audio using Hugging Face models, summarize the transcription, and download the summary as a PDF.

## Features
- **Live Audio Recording**: Record lectures or any audio directly through the browser.
- **Automatic Transcription**: The app uses the Hugging Face `wav2vec2` model to convert the recorded audio to text.
- **Text Summarization**: The transcription is summarized using Hugging Face's `bart-large-cnn` model.
- **Downloadable Output**: Users can download the summarized transcription (as a PDF).

## How It Works
1. **Record**: Click the "Start Recording" button to record live audio directly from the browser.
2. **Stop**: After you finish recording, click the "Stop Recording" button.
3. **Processing**: The app transcribes the audio and generates a summary of the transcription.
4. **Download**: Download the summary as a PDF.

## Technologies Used
- **Python 3.8+**
- **Flask**: Web framework used to create the backend server.
- **Pydub**: Used for handling audio conversion.
- **FPDF**: For generating PDF files.
- **Hugging Face Transformers**: For automatic speech recognition (`wav2vec2`) and summarization (`bart-large-cnn`).
- **MediaRecorder API**: To record audio on the client-side in the browser.
- **HTML, CSS, JavaScript**: Frontend components to handle audio recording and interaction with the Flask backend.

