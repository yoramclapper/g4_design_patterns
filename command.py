from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class Backlog:

    def __init__(self):
        self._backlog = []

    def add_command(self, client: str, command: Command):
        self._backlog.append((client, command))

    def remove_command(self, client: str, command: Command):
        self._backlog.remove((client, command))

    def next_command(self):
        if self._backlog:
            return self._backlog[0]
        else:
            return None


class Manager:

    def __init__(self, name, backlog: Backlog):
        self._name = name
        self._backlog = backlog

    def send_request(self, command: Command):
        self._backlog.add_command(client=self._name, command=command)

    def cancel_request(self, command: Command):
        self._backlog.remove_command(client=self._name, command=command)


class Worker:

    def __init__(self, backlog: Backlog):
        self._current_task = None
        self._backlog = backlog

    def get_next_task(self):
        self._current_task = self._backlog.next_command()

    def workon_task(self):
        if self._current_task:
            return self._current_task[1].execute()
        else:
            return "No task available..."

    def finish_task(self):
        if self._current_task:
            self._backlog.remove_command(client=self._current_task[0], command=self._current_task[1])



class Develop(Command):

    def __init__(self, description: str):
        self._description = description

    def execute(self):
        return f"Developing: {self._description}"


class Query(Command):

    def __init__(self, description: str):
        self._description = description

    def execute(self):
        return f"Querying: {self._description}"


class Automate(Command):

    def __init__(self, description: str):
        self._description = description

    def execute(self):
        return f"Automating: {self._description}"


if __name__ == "__main__":

    backlog = Backlog()

    manager = Manager(name="Manager", backlog=backlog)
    worker = Worker(backlog=backlog)

    automate_hiring = Automate(description="hiring")
    develop_portal = Develop(description="portal")
    develop_api = Develop(description="API")
    query_revenue = Query(description="revenue")

    manager.send_request(command=automate_hiring)
    manager.send_request(command=develop_portal)
    manager.send_request(command=develop_api)
    manager.cancel_request(command=automate_hiring)
    manager.send_request(command=query_revenue)

    for _ in range(len(backlog._backlog)):
        worker.get_next_task()
        print(
            worker.workon_task()
        )
        worker.finish_task()




