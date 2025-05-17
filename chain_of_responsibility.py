from abc import ABC, abstractmethod

class RestaurantEmployee(ABC):

    def __init__(self):
        self._next_handler = None

    def set_next_handler(self, handler: 'RestaurantEmployee') -> 'RestaurantEmployee':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, request: str):
        pass


class Cook(RestaurantEmployee):

    def handle_request(self, request: str):
        if request == "meal":
            return "Cook started preparing meal..."

        elif self._next_handler:
            return self._next_handler.handle_request(request=request)

        return "Request couldn't be handled"


class Waitress(RestaurantEmployee):

    def handle_request(self, request: str):
        if request == "bill":
            return "Waitress is fetching bill..."

        elif request == "beverage":
            return "Waitress is fetching beverage..."

        elif self._next_handler:
            return self._next_handler.handle_request(request=request)

        else:
            return "Request couldn't be handled..."


if __name__ == "__main__":

    waitress = Waitress()
    cook = Cook()

    waitress.set_next_handler(cook)

    request = "meal"
    print(
        waitress.handle_request(request=request)
    )

