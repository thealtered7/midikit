import mido

def output_tracks(midi_file: mido.MidiFile):
    tracks = midi_file.tracks
    print("number of tracks: {}".format(len(tracks)))

    for track in tracks:
        print("track name: {}, number of events: {}".format(track.name, len(track)))
        for event in track:
            print(event)
        input("press a thing to continue... ")



def main():
    file_name = "/home/jkeene/Music/midi/bach/johan_sebastion/keyboard/suite/english/bwv807/bwv807a.mid"
    midi_file = mido.MidiFile(file_name)
    #output_tracks(midi_file)
    for event in midi_file:
        print(event)
        input("continue... ")


if __name__ == "__main__":
    main()
