import pydantic
from mido import MidiTrack, MidiFile, Message


def is_note_on(message: Message) -> bool:
    return message.type == 'note_on'


def is_note_off(message: Message) -> bool:
    return message.type == 'note_off'


class MidiFileStats(pydantic.BaseModel):
    track_count: int

class MidiTrackStats(pydantic.BaseModel):
    track_number: int
    minimum_pitch: int
    maximum_pitch: int
    first_pitch: int
    last_pitch: int
    pitch_count: int


def get_midi_track_stats(midi_track: MidiTrack, track_number: int) -> MidiTrackStats:
    minimum_pitch = 10000
    maximum_pitch = 0
    first_pitch = 0
    last_pitch = 0
    pitch_count = 0

    for i, event in enumerate(midi_track):
        if type(event) == Message:
            e: Message = event



    stats = MidiTrackStats(
        track_number=track_number,
        last_pitch=last_pitch,
        first_pitch=first_pitch,
        pitch_count=pitch_count,
        minimum_pitch=minimum_pitch,
        maximum_pitch=maximum_pitch
    )

    return stats

def main():
    path = "/home/jkeene/Music/midi/bach/johan_sebastion/keyboard/suite/english/bwv807/bwv807a.mid"
    midi_file = MidiFile(filename=path)
    stats_list = [get_midi_track_stats(midi_track=midi_track, track_number=i) for i, midi_track in enumerate(midi_file.tracks)]
    for stats in stats_list:
        print(stats)


if __name__ == "__main__":
    main()

