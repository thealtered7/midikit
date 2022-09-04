from collections import Counter
import sys
import pydantic
from midikit.music.pitch_class import pitch_class
from typing import Iterable, Callable, Optional, Dict
from mido import MidiTrack, MidiFile, Message, MetaMessage

import pprint


def update_pitch_measure(current_measure: int, candidate_measure: int, fun: Callable) -> int:
    if current_measure is None:
        return candidate_measure
    else:
        return fun(current_measure, candidate_measure)


def is_note_on(message: Message) -> bool:
    return message.type == 'note_on'


def is_note_off(message: Message) -> bool:
    return message.type == 'note_off'


class MidiTrackStats(pydantic.BaseModel):
    track_number: int
    minimum_pitch: Optional[int]
    maximum_pitch: Optional[int]
    first_pitch: Optional[int]
    last_pitch: Optional[int]
    pitch_counter: Counter
    pitch_class_counter: Counter
    event_type_counter: Counter

    def pretty_print(self, stream=sys.stdout):
        printer = pprint.PrettyPrinter(stream=stream, compact=False)
        printer.pprint(self.__dict__)


class MidiFileStats(pydantic.BaseModel):
    track_count: int
    track_stats: Dict[int, MidiTrackStats]
    filename: str

    def pretty_print(self, stream=sys.stdout):
        printer = pprint.PrettyPrinter(stream=stream, compact=False)
        printer.pprint(self.__dict__)


def get_midi_file_stats(midi_file: MidiFile) -> MidiFileStats:
    track_stats = {}
    track_count = 0
    midi_file.filename

    for i, track in enumerate(midi_file.tracks):
        track_count = i
        track_stat = get_midi_track_stats(midi_track=track, track_number=i)
        track_stats[i] = track_stat

    return MidiFileStats(
        track_count=track_count,
        track_stats=track_stats,
        filename=midi_file.filename,
    )


def get_midi_track_stats(midi_track: MidiTrack, track_number: int) -> MidiTrackStats:
    minimum_pitch = None
    maximum_pitch = None
    first_pitch = None
    last_pitch = None
    pitch_counter = Counter()
    pitch_class_counter = Counter()
    event_type_counter = Counter()

    for i, event in enumerate(midi_track):
        event_type_counter.update([event.type])
        if is_note_on(event):
            pitch = event.note
            pitch_counter.update([pitch])
            pitch_class_counter.update([pitch_class(pitch)])
            maximum_pitch = update_pitch_measure(current_measure=maximum_pitch,
                                                 candidate_measure=event.note,
                                                 fun=max)
            minimum_pitch = update_pitch_measure(current_measure=minimum_pitch,
                                                 candidate_measure=event.note,
                                                 fun=min)
            if first_pitch is None:
                first_pitch = event.note
            last_pitch = event.note

    stats = MidiTrackStats(
        track_number=track_number,
        last_pitch=last_pitch,
        first_pitch=first_pitch,
        minimum_pitch=minimum_pitch,
        maximum_pitch=maximum_pitch,
        event_type_counter=event_type_counter,
        pitch_counter=pitch_counter,
        pitch_class_counter=pitch_class_counter,
    )

    return stats


def find_messages_of_type(message_type: str, messages: Iterable[Message]) -> Iterable[Message]:
    return (m for m in messages if m.type == message_type)


def main():
    path = "/home/jkeene/Music/midi/bach/johan_sebastion/keyboard/suite/english/bwv807/bwv807a.mid"
    midi_file = MidiFile(filename=path)
    file_stats = get_midi_file_stats(midi_file=midi_file)
    file_stats.pretty_print(stream=sys.stdout)


if __name__ == "__main__":
    main()

