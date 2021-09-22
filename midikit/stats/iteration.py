from typing import Generator, List
from mido import (
    MidiFile,
    MidiTrack
)


def create_track_generator(midi_file: MidiFile, track_list: List[int] = []) -> Generator[MidiTrack, None, None]:
    if not track_list:
        track_list = range(0, len(midi_file.tracks))

    for i, track in enumerate(midi_file.tracks):
        if i in track_list:
            yield track
