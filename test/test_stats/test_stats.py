import unittest
from pytest import mark
from mido import Message, MetaMessage
from midikit.stats.stats import is_note_on, is_note_off, find_messages_of_type


@mark.parametrize("message,expected", [(Message('note_on', note=40), True),
                                       (Message('note_off', note=40), False)])
def test_is_note_on(message, expected):
    assert is_note_on(message) == expected


@mark.parametrize("message,expected", [(Message('note_on', note=40), False),
                                       (Message('note_off', note=40), True)])
def test_is_note_off(message, expected):
    assert is_note_off(message) == expected


def test_find_messages_of_type_time_signature():
    messages = [Message(type="note_on", note=40),
                MetaMessage(type="time_signature",
                            numerator=3,
                            denominator=4,
                            clocks_per_click=24,
                            notated_32nd_notes_per_beat=8,
                            time=0)]
    found_messages = list(find_messages_of_type(message_type="time_signature", messages=messages))
    assert len(found_messages) == 1


def test_find_messages_of_type_note_on():
    messages = [Message(type="note_on", note=40),
                MetaMessage(type="time_signature",
                            numerator=3,
                            denominator=4,
                            clocks_per_click=24,
                            notated_32nd_notes_per_beat=8,
                            time=0),
                Message(type="note_on", note=40),
                ]
    found_messages = list(find_messages_of_type(message_type="note_on", messages=messages))
    assert len(found_messages) == 2