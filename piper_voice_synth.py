import numpy as np
import sounddevice as sd
import io
from piper.voice import PiperVoice

model = "C:/Abishek/mypy/TALK2ME/Resources/en_US-john-medium.onnx"
voice = PiperVoice.load(model)
text = "Archaeology is indeed the scientific study of human history and prehistory through the systematic excavation and analysis of sites and the material remains (artifacts, architecture, biofacts, and cultural landscapes) that people have left behind."

# Setup a sounddevice OutputStream with appropriate parameters
# The sample rate and channels should match the properties of the PCM data
stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
stream.start()

for audio_bytes in voice.synthesize_stream_raw(text):
    ##buffer = io.BytesIO()
    int_data=np.frombuffer(audio_bytes, dtype=np.int16)
    ##audio_bytes=buffer.getvalue()
    stream.write(int_data)

stream.stop()
stream.close()
