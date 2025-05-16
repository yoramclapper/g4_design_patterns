from abc import ABC, abstractmethod

class Character(ABC):

    @abstractmethod
    def write(self, color: str) -> str:
        pass

class LetterA(Character):

    def __init__(self):
        self._char = 'A'

    def write(self, color: str) -> str:
        return f'Write {color} {self._char}'


class LetterB(Character):

    def __init__(self):
        self._char = 'B'

    def write(self, color: str) -> str:
        return f'Write {color} {self._char}'


class CharacterFactory:

    def __init__(self):
        self._chars = dict()


    def get_char(self, char_key: str):
        if char_key in self._chars:
            return self._chars[char_key]
        elif char_key == 'A':
            self._chars[char_key] = LetterA()
            return self._chars[char_key]
        elif char_key == 'B':
            self._chars[char_key] = LetterB()
            return self._chars[char_key]
        else:
            raise ValueError("Entered character is unavailable")


if __name__ == '__main__':
    character_factory = CharacterFactory()

    letter_a = character_factory.get_char('A')
    print(letter_a.write(color='red'))
    letter_b = character_factory.get_char('B')
    print(letter_b.write(color='blue'))
    letter_c = character_factory.get_char('C')


