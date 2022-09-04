from abc import abstractmethod, abstractproperty


class DurationException(Exception):
    def __init__(self, msg: str):
        Exception.__init__(self, msg)


class ConsumeDurationResult:
    consumption_requested: int
    consumed: int
    remaining: int


class HasDuration:
    @abstractmethod
    def consume(self, duration: int) -> ConsumeDurationResult:
        raise NotImplemented()

    @abstractproperty
    def duration_remaining(self) -> int:
        raise NotImplemented()

    @abstractproperty
    def duration_consumed(self) -> int:
        raise NotImplemented()

    @abstractproperty
    def duration(self) -> int:
        raise NotImplemented()

    @abstractproperty
    def totally_consumed(self) -> bool:
        raise NotImplemented()

    @abstractproperty
    def partially_consumed(self) -> bool:
        raise NotImplemented()


class InfiniteDuration(HasDuration):
    _consumed: int = 0

    def __init__(self):
        HasDuration.__init__(self)
        self._consumed = 0

    @property
    def duration_remaining(self) -> int:
        pass

    @property
    def duration_consumed(self) -> int:
        pass

    @property
    def duration(self) -> int:
        pass

    @property
    def totally_consumed(self) -> bool:
        pass

    @property
    def partially_consumed(self) -> bool:
        pass

    def consume(self, duration: int) -> ConsumeDurationResult:
        pass





