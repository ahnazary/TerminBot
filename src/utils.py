import os

def beep():
    duration = 0.5  # seconds
    freq = 350  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

beep()