import unittest
from mido import MidiTrack, MidiFile
from midikit.stats.iteration import create_track_generator

TEST_FILE_PATH = "/home/jkeene/Music/midi/bach/johan_sebastion/keyboard/suite/english/bwv807/bwv807a.mid"


class MyTestCase(unittest.TestCase):
    def test_create_track_generator(self):
        midi_file = MidiFile(filename=TEST_FILE_PATH)
        tracks = list(create_track_generator(midi_file=midi_file))
        self.assertEqual(len(tracks), len(midi_file.tracks))

    def test_create_track_generator_with_track_list(self):
        tracks_to_skip = [2, 3]
        midi_file = MidiFile(filename=TEST_FILE_PATH)
        track_list = [x for x in range(0, len(midi_file.tracks)) if x not in tracks_to_skip]
        tracks = list(create_track_generator(midi_file=midi_file, track_list=track_list))
        names_expect = set([track.name for (i, track) in enumerate(midi_file.tracks) if i not in tracks_to_skip])
        names_actual = set([track.name for track in tracks])
        self.assertEqual(names_actual, names_expect)




if __name__ == '__main__':
    unittest.main()
