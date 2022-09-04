import unittest
import pytest

from midikit.music.pitch_class import PitchException, pitch_class


def test_less_than_zero():
    with pytest.raises(PitchException):
        pitch_class(-1)


@pytest.mark.parametrize('pitch,expect', list([(i, i % 12) for i in range(0, 120)]))
def test_pitch_class(pitch: int, expect: int):
    assert pitch_class(pitch) == expect


if __name__ == '__main__':
    unittest.main()
