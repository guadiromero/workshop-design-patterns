"""
An implementation without using any Design Patterns,
"""
class NewsChannel:
    def __init__(self):
        self.messages = []

    def publish_message(self, message):
        self.messages.append(message)


class Employee:
    def __init__(self, name):
        self.name = name

    def retrieve_messages(self, news_channel):
        print(f"NEWS FOR {self.name}:")
        for message in news_channel.messages:
            print(message)


# Client code
office_news = NewsChannel()
funny_news = NewsChannel()

billy = Employee("BILLY")
mandy = Employee("MANDY")
grim = Employee("GRIM")

office_news.publish_message("Run out of toilet paper!")
funny_news.publish_message("Why do ghosts ride the elevator? To lift their spirits.")

billy.retrieve_messages(office_news)
billy.retrieve_messages(funny_news)
