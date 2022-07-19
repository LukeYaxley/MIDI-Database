import mido
from mido import MidiFile


def readFile(filename):
    mid = MidiFile('./test files/{}.mid'.format(filename), clip=True)
    print(mid)
readFile("ABBA_-_SOS")