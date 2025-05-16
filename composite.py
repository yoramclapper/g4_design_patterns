from abc import ABC, abstractmethod

class Garment(ABC):

    def __init__(self, name: str):
        self._name = name

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def dress_up(self) -> str:
        pass

    @abstractmethod
    def add(self, garment: 'Garment'):
        pass

    @abstractmethod
    def remove(self, garment: 'Garment'):
        pass


class Shirt(Garment):

    def __init__(self, name: str):
        super().__init__(name)

    @property
    def name(self) -> str:
        return self._name

    def dress_up(self) -> str:
        return f"Wearing a {self._name} shirt."

    def add(self, garment: 'Garment'):
        raise NotImplementedError("Cannot add to a shirt.")

    def remove(self, garment: 'Garment'):
        raise NotImplementedError("Cannot remove from a shirt.")

class Pants(Garment):
    def __init__(self, name: str):
        super().__init__(name)

    @property
    def name(self) -> str:
        return self._name

    def dress_up(self) -> str:
        return f"Wearing {self._name} pants."

    def add(self, garment: 'Garment'):
        raise NotImplementedError("Cannot add to pants.")

    def remove(self, garment: 'Garment'):
        raise NotImplementedError("Cannot remove from pants.")


class Outfit(Garment):
    def __init__(self, name: str):
        super().__init__(name)
        self._garments = []

    @property
    def name(self) -> str:
        return self._name

    def dress_up(self) -> str:
        outfit_description = f"Wearing {self._name} outfit with: "
        for garment in self._garments:
            outfit_description += f"\n- {garment.dress_up()}"
        return outfit_description

    def add(self, garment: 'Garment'):
        self._garments.append(garment)

    def remove(self, garment: 'Garment'):
        self._garments.remove(garment)


if __name__ == "__main__":
    shirt = Shirt("blue")
    pants = Pants("black")

    outfit = Outfit("casual")
    outfit.add(shirt)
    outfit.add(pants)

    print(outfit.dress_up())

    outfit.remove(pants)

    print(outfit.dress_up())






