# %%
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise

# %%

data, rate = sf.read("Cancelation/audios/Wherever.wav")
data = data
# %%
reduced_stat = nr.reduce_noise(y = data.T, sr=rate, n_std_thresh_stationary=1.5,stationary=True)

# %%
reduced_nonstat = nr.reduce_noise(y = data.T, sr=rate, thresh_n_mult_nonstationary=2,stationary=False)

# %%
wavfile.write("Cancelation/tests/Wherever_stationary.wav", rate, reduced_stat.T)
wavfile.write("Cancelation/tests/Wherever_NonStationary.wav", rate, reduced_nonstat.T)