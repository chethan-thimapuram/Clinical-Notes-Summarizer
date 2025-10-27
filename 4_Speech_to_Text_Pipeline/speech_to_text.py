# Demo placeholder for a speech-to-text pipeline.
# For an offline lightweight demo we show how to call OpenAI Whisper if available locally.
# To keep this demo laptop-friendly we simply show a pseudo-function.

def transcribe_demo(audio_path):
    # In real project: call a model like whisper or Google Speech-to-Text API.
    # Here we simulate by returning a fixed transcript.
    return "Simulated transcript: Patient reports headache and nausea for two days."

if __name__ == '__main__':
    print(transcribe_demo('sample_audio.wav'))
