import mido

def output_tracks(midi_file: mido.MidiFile):
    tracks = midi_file.tracks
    print("number of tracks: {}".format(len(tracks)))

    for track in tracks:
        print("track name: {}, number of events: {}".format(track.name, len(track)))


def main():
    file_name = "/home/jkeene/Downloads/01_Premonition.mid"
    midi_file = mido.MidiFile(file_name)
    output_tracks(midi_file)


if __name__ == "__main__":
    main()
