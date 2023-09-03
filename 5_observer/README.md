# 5. Observer

The observer is a **behavioral** design pattern that works as a publish-subscribe mechanism. When the object changes, it notifies all its subscribers automatically.

## A simple example

### Before

Billy, Mandy and Grim work at the same office, and they want to build an app to keep updated about the current events in the building. Billy also really wants to receive funny jokes once in a while, because it makes his workday more fun. However, Mandy and Grim get annoyed by such jokes and don't want to get spammed all the time. They decide to make two different news channels, so that anyone can subscribe to whatever news they are interested in.

```python
class NewsChannel:
    def __init__(self):
        self.messages = []

    def update(self, message):
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

office_news.update("Run out of toilet paper!")
funny_news.update("Why do ghosts ride the elevator? To lift their spirits.")

billy.retrieve_messages(office_news)
billy.retrieve_messages(funny_news)
```

```
# Output

NEWS FOR BILLY:
Run out of toilet paper!

NEWS FOR BILLY:
Why do ghosts ride the elevator? To lift their spirits.
```

They are not satisfied with this implementation, though, as they need to check all the time the channels to see if there are any new messages. They would prefer to receive notifications automatically whenever there are new messages in the channels they are interested in.

### After

The Observer pattern is perfect for this use case. On the one hand we have a *subject* or *publisher* with some interesting state or stream of events it publishes. In our example, the subject is the class `NewsChannel`, which publishes incoming news. On the other hand, we have an *observer* or *subscriber*. In our specific case, the observers are the objects of class `Employee` that want to keep track of the news.  We can refactor our code using the Observer pattern like in the example below.

```python
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
```

```
# Output

NEWS FOR GRIM: Run out of toilet paper!
NEWS FOR MANDY: Run out of toilet paper!
NEWS FOR BILLY: Run out of toilet paper!
NEWS FOR BILLY: Why do ghosts ride the elevator? To lift their spirits.
```

The publisher `NewsChannel` stores a list of `subscribers` and provides methods so that the employees can `subscribe()` or `unsubscribe()` from that list. Whenever there is an update in its state, the publisher goes over its list of subscribers and calls their update methods to send notifications. This is what happens in the `publish_message()` method of `NewsChannel`. It iterates over every employee in the subscribers list and calls their `update()` methods, which send the appropriate notifications. In this way, the notification is sent automatically right after a new message is published, and there is no need for the employees to manually check a `NewsChannel` for new messages.
