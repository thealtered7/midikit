import unittest
from pytest import mark
from mido import Message
from midikit.stats.stats import is_note_on, is_note_off


@mark.parametrize("message,expected", [(Message('note_on', note=40), True),
                                       (Message('note_off', note=40), False)])
def test_is_note_on(message, expected):
    assert is_note_on(message) == expected


@mark.parametrize("message,expected", [(Message('note_on', note=40), False),
                                       (Message('note_off', note=40), True)])
def test_is_note_off(message, expected):
    assert is_note_off(message) == expected




