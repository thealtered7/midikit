NUMBER_OF_PITCH_CLASSES = 12


class PitchException(Exception):
    pitch: int
    message: str

    def __init__(self, message: str):
        Exception.__init__(self, message)

    def __str__(self) -> str:
        pitch = self.pitch
        message = self.message
        return f"{pitch=}: {message}"


def create_pitch_exception(message: str, pitch: int) -> PitchException:
    exception = PitchException(message=message)
    exception.pitch = pitch
    return exception


def pitch_class(pitch: int) -> int:
    if pitch < 0:
        raise create_pitch_exception(message="pitch is < 0", pitch=pitch)

    return pitch % NUMBER_OF_PITCH_CLASSES
