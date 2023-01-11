from simple_diarizer.diarizer import Diarizer
from simple_diarizer.utils import (check_wav_16khz_mono, convert_wavfile,
                                   waveplot, combined_waveplot, waveplot_perspeaker)

import os
import tempfile
from pprint import pprint

import matplotlib.pyplot as plt
import soundfile as sf

from IPython.display import Audio, display, HTML, IFrame
from tqdm.autonotebook import tqdm

from pytube.extract import video_id
import subprocess
import validators


def get_youtube_id(url):
    return video_id(url)

def download_youtube_wav(youtube_id, outfolder='./', overwrite=True):
    if validators.url(youtube_id):
        youtube_id = video_id(youtube_id)

    os.makedirs(outfolder, exist_ok=True)

    outfile = os.path.join(outfolder, '{}.wav'.format(youtube_id))
    if not overwrite:
        if os.path.isfile(outfile):
            return outfile

    cmd = "youtube-dl --no-continue --extract-audio --audio-format wav -o '{}' {}".format(
        outfile, youtube_id)
    subprocess.Popen(cmd, shell=True).wait()

    assert os.path.isfile(outfile), "Couldn't find expected outfile, something went wrong"
    return outfile


def diarize_yt(youtube_url, diar, ns=None):
    youtube_id = get_youtube_id(youtube_url)
    with tempfile.TemporaryDirectory() as outdir:
        print("Downloading wav file...")
        yt_file = download_youtube_wav(youtube_id, outdir)

        wav_file = convert_wavfile(yt_file, f"{outdir}/{youtube_id}_converted.wav")
        signal, fs = sf.read(wav_file)

        print(f"Diarizing {youtube_id}...")
        segments = diar.diarize(wav_file, 
                                num_speakers=ns,
                                outfile=f"{outdir}/{youtube_id}.rttm")
        return segments, (signal, fs)


def main():
    diar = Diarizer(
                    embed_model='ecapa', # supported types: ['xvec', 'ecapa']
                    cluster_method='sc', # supported types: ['ahc', 'sc']
                    window=1.5, # size of window to extract embeddings (in seconds)
                    period=0.75 # hop of window (in seconds)
                    )

    iasip_video = "https://www.youtube.com/watch?v=ghrdSTC66MA"
    iasip_segments, (iasip_signal, fs) = diarize_yt(iasip_video, diar, 2)

    waveplot_perspeaker(iasip_signal, fs, iasip_segments)
    
if __name__ == "__main__":
    main()