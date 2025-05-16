from abc import ABC, abstractmethod

class Cake(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def bake(self):
        pass


class ChocolateCake(Cake):

    @property
    def name(self) -> str:
        return "chocolate cake"

    def bake(self) -> str:
        return f"Baking {self.name}"


class DecoratedCake(Cake):

    def __init__(self, cake: Cake):
        self._cake = cake

    @property
    def name(self) -> str:
        return self._cake.name

    def bake(self):
        return self._cake.bake()


class DecoratedCakeWithCandles(DecoratedCake):

    def __init__(self, cake: Cake):
        super().__init__(cake=cake)

    def bake(self):
        return f"{self._cake.bake()} + adding candles"


class DecoratedCakeWithGlaze(DecoratedCake):

    def __init__(self, cake: Cake):
        super().__init__(cake=cake)

    def bake(self):
        return f"{self._cake.bake()} + adding glaze"


if __name__ == "__main__":
    cake = ChocolateCake()
    cake = DecoratedCakeWithCandles(cake=cake)
    cake = DecoratedCakeWithGlaze(cake=cake)

    print(cake.bake())