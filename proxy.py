from abc import ABC, abstractmethod

class Speech(ABC):

    @abstractmethod
    def start_talking(self) -> str:
        pass


class SmallTalk(Speech):

    def __init__(self, name: str):
        self._name = name

    def start_talking(self) -> str:
        return f"Hi, my name is {self._name}."


class SmallTalkProxy(Speech):

    def __init__(self, name: str, partner: str):
        self._name = name
        self._partner = partner
        self._cache = None

    def start_talking(self) -> str:
        if self._partner == "Crush":
            return "Panick!"

        if self._cache is not None:
            print("Get result from cache...")
            return self._cache

        small_talk = SmallTalk(name=self._name)
        self._cache = small_talk.start_talking()
        return self._cache


if __name__ == '__main__':
    proxy = SmallTalkProxy(name="John", partner="Pete")
    print(
        proxy.start_talking()
    )
    print(
        proxy.start_talking()
    )
