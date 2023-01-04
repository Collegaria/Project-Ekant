# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def recorder(freq,duration,path):
# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write(f"{path}_init.wav", freq, recording)
# Convert the NumPy array to audio file
wv.write(f"{path}_final.wav", recording, freq, sampwidth=2)

def main():
    # Sampling frequency
    freq = 44100
    # Recording duration
    duration = 5
    path = "recording/audioData"
if __name__ == "__main__":
    main()