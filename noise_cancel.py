from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise


def callAudio(audio):
    data, rate = sf.read(audio)
    return data, rate

def statCall(data, rate):
    reduced_stat = nr.reduce_noise(y = data.T, sr=rate, n_std_thresh_stationary=1.5,stationary=True)
    return reduced_stat.T


def nonstatCall(data, rate):
    reduced_nonstat = nr.reduce_noise(y = data.T, sr=rate, thresh_n_mult_nonstationary=2,stationary=False)
    return reduced_nonstat.T

def saver(type, rate, name):
    wavfile.write(f"Cancelation/tests/{name}.wav", rate, type)

def main():
    aData, aRate = callAudio("Cancelation/audios/Wherever.wav")
    stat = statCall(aData, aRate)
    nonstat = nonstatCall(aData, aRate)
    
    saver(stat, aRate, "Wherever_stat")
    saver(nonstat, aRate, "Wherever_nonstat")
    

if __name__ == "__main__":
    main()