#using noisereduce
from scipy.io import wavfile
import noisereduce as N_Red
# load data
rat_E, DatA = wavfile.read("Cancelation_audios_Whenever.wav")
# perform noise reduction
reducNo = N_Red.reduce_noise(y=DatA, sr=rat_E)
wavfile.write("x.wav", rat_E, reducNo)

