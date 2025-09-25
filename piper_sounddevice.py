import os, sys, gc, datetime, tracemalloc
from memory_profiler import profile

import sounddevice as sd
import soundfile as sf
import wave

from piper.voice import PiperVoice
from io import BytesIO
import numpy as np


##filename = 'temp.wav'
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


dt=datetime.datetime
print(f"Begin Script:{dt.now()}")

#model = "./resources/en_US-john-medium.onnx"
model = "./resources/en_US-danny-low.onnx"
voice = PiperVoice.load(model)

text1 = "This temporary wave file was generated from Python call to piper output to python sound device"
#snapshot = tracemalloc.take_snapshot()
#top_stats = snapshot.statistics('lineno')

@profile
def speakit(text):
	tracemalloc.start()
	audio=BytesIO()
	
	snapshot = tracemalloc.take_snapshot()
	top_stats = snapshot.statistics('lineno')

	with wave.open(audio, 'w') as wav_file:
		wav_file.setnchannels(2)
		wav_file.setsampwidth(2)
		wav_file.setframerate(44100)
		print(f"Begin SynthV:{dt.now()}")
		voice.synthesize_wav(text, wav_file)
		print(f"End SynthV:{dt.now()}")
		print(audio.getbuffer().nbytes)
		wav_file.close()
	##audio = voice.synthesize(text,wav_file)
	
	# Extract data and sampling rate from file
	##data, fs = sf.read(filename, dtype='float32')
	audio.seek(0)
	data, fs = sf.read(audio)
	print(f"Begin Speak:{dt.now()}")
	sd.play(data, fs)
	status = sd.wait()  # Wait until file is done playing
	print(f"End Speak:{dt.now()}")
	##os.remove(filename)
	snapshot = tracemalloc.take_snapshot()
	top_stats = snapshot.statistics('lineno')
	for stat in top_stats[:10]:
		print(stat)
	#gc.collect()
	#data=None
	#audio=None

speakit(text)
print(f"End Script:{dt.now()}")

while (1):
	text = input()
	speakit(text)	

#snapshot = tracemalloc.take_snapshot()
#top_stats = snapshot.statistics('lineno')

#for stat in top_stats[:10]:
#	print(stat)
