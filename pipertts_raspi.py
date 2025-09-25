# Text-To-Speech Translation with Piper TTS and Python
# TechMakerAI on YouTube
from piper import PiperVoice
import wave
import sys
import datetime 

from io import BytesIO
from pygame import mixer

dt=datetime.datetime
mixer.init()
mp3audio = BytesIO()
audio_file='D:/Abishek/TALK2ME/sample/ttstest.wav'

voice = PiperVoice.load('C:/Abishek/mypy/TALK2ME/Resources/en_US-john-medium.onnx',
	config_path='C:/Abishek/mypy/TALK2ME/Resources/en_US-john-medium.onnx.json')

print(mp3audio.getbuffer().nbytes)

print(f"{sys.argv[1:]}")
n = len(sys.argv)

str=""

if (n==1):
	str="A rainbow is a meteorological phenomenon that is caused by reflection, refraction and dispersion of light in water droplets resulting in a spectrum of light appearing in the sky."
else:	
	for i in range(1, n):
		str+=sys.argv[i] + " "

##print(f"Number of words {n}")
print(f"Line to speak : {str}")

text = str

#wav_file = wave.open(audio_file, "wb")
#wav_file.setnchannels(2)
#wav_file.setsampwidth(2)
#wav_file.setframerate(44100)

#audio = voice.synthesize_wav(text, wav_file)
##print (voice.synthesize_stream_raw(text))
#wav_file.close()

def synthvoice(wavbuff1, speaktext):
  wavbuff=BytesIO()
  with wave.open(wavbuff, "wb") as wav_file:
    wav_file.setnchannels(2)
    wav_file.setsampwidth(2)
    wav_file.setframerate(44100)
    voice.synthesize_wav(speaktext, wav_file)
    print(wavbuff.getbuffer().nbytes)
    wav_file.close()
    return wavbuff

def speakit(mp3audio):		
  mp3audio.seek(0)
  print(mp3audio.getbuffer().nbytes)
  mixer.music.load(mp3audio, "wav")
  #mixer.music.load(audio_file, "wav")
  mixer.music.play()
  
  while mixer.music.get_busy():
    pass

def runitall(text):
  mp3audio=BytesIO()		
  print(f"Begin SynthV:{dt.now()}")
  ##synthvoice(mp3audio, text)
  mp3audio=synthvoice(mp3audio,text)
  print(f"End SynthV:{dt.now()}")
  print(f"Begin Speak:{dt.now()}")
  speakit(mp3audio)
  print(f"End Speak:{dt.now()}")




with wave.open(mp3audio, "wb") as wav_file:
	wav_file.setnchannels(2)
	wav_file.setsampwidth(2)
	wav_file.setframerate(44100)
	voice.synthesize_wav(text, wav_file)
	print(mp3audio.getbuffer().nbytes)
	wav_file.close()

mp3audio.seek(0)
print(mp3audio.getbuffer().nbytes)
mixer.music.load(mp3audio, "wav")
#mixer.music.load(audio_file, "wav")
mixer.music.play()

while mixer.music.get_busy():
	pass
