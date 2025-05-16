class Kettle:

    def fill(self):
        return "Fill kettle with water..."

    def on(self):
        return "Water is heating up..."

    def add_tea(self):
        return "Add tea to kettle..."

class CoffeeGrinder:

    def fill(self):
        return "Fill grinder with coffee beans..."

    def on(self):
        return "Grinding coffee beans..."


class CoffeeFilter:

    def percolate(self):
        return "Percolate coffee.."


class Dispenser:

    def __init__(self, kettle: Kettle, grinder: CoffeeGrinder, filter: CoffeeFilter):
        self._kettle = kettle
        self._grinder = grinder
        self._filter = filter

    def make_tea(self):
        return f"Started making tea:\n{self._kettle.fill()}\n{self._kettle.on()}\n{self._kettle.add_tea()}"

    def make_coffee(self):
        return f"Started making coffee:\n{self._kettle.fill()}\n{self._kettle.on()}\n{self._grinder.fill()}\n{self._grinder.on()}\n{self._filter.percolate()}"

if __name__ == '__main__':

    kettle = Kettle()
    grinder = CoffeeGrinder()
    filter = CoffeeFilter()
    dispenser = Dispenser(kettle=kettle, grinder=grinder, filter=filter)
    print(dispenser.make_tea())
    print("\n")
    print(dispenser.make_coffee())