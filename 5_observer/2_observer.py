"""
An implementation using the Observer Design Pattern.
"""
class NewsChannel:
    def __init__(self):
        self.subscribers = set()

    def subscribe(self, employee):
        self.subscribers.add(employee)
        return

    def unsubscribe(self, employee):
        self.subscribers.remove(employee)
        return

    def publish_message(self, message):
        for employee in self.subscribers:
            employee.update(message)


class Employee:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"NEWS FOR {self.name}: {message}")
        return


# Client code
office_news = NewsChannel()
funny_news = NewsChannel()

billy = Employee("BILLY")
mandy = Employee("MANDY")
grim = Employee("GRIM")

office_news.subscribe(billy)
office_news.subscribe(mandy)
office_news.subscribe(grim)
funny_news.subscribe(billy)

office_news.publish_message("Run out of toilet paper!")
funny_news.publish_message("Why do ghosts ride the elevator? To lift their spirits.")
