import mido
from mido import MidiFile


def readFile(filename):
    mid = MidiFile('./test files/{}.mid'.format(filename), clip=True) #opens Midi file with name given in function parameter
    notes = []
    for msg in mid:
        if msg.type == "note_on":# checks to see whether the note is one being pressed down or released only pressed down we want to see
            #print(msg)
            notes.append(msg.note)
            #print(msg.note)
    return(notes)
def compareNotes(notes1,notes2):
    length = len(notes1)
    similarity =0
    #print("got here")
    for i in range(len(notes1)):
        if notes1[i]== notes2[i]:
            similarity += 1
    #print(similarity)
    return(similarity/length)


def check(query,arr):
# checks to see if the query is in the array
  if len(arr) < 3:
    return False
  for i in range(len(arr)-2):
    #print(arr[i:i+3])
    if arr[i:i+3] == query:
      return True
  return False
#print(compareNotes(readFile("ABBA_-_SOS"),readFile("ABBA_-_SOS"))) #test statement
#print(readFile("ABBA_-_SOS")[14:20])
print(check([53,57,50], readFile("ABBA_-_SOS")))
#print(readFile("ABBA_-_SOS")[67])