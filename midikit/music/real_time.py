from mido import MidiFile
import sys

MIDI_FILE_PATH = "/home/jkeene/Music/midi/bach/johan_sebastion/keyboard/suite/english/bwv807/bwv807a.mid"
MIDI_FILE_PATH = "/home/jkeene/Music/midi/experiments/Experiment_2.mid"





def main():
    output_stream = sys.stdout
    midi_file = MidiFile(filename=MIDI_FILE_PATH)
    midi_file.print_tracks(meta_only=True)
    for message in midi_file.play():
        print(message, file=output_stream)


if __name__ == "__main__":
    main()



