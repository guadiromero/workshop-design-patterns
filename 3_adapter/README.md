# 3. Adapter

The Adapter is a **structural** design pattern that allows classes with incompatible interfaces to work together.

## A simple example

### Before

Let's suppose we have an API with a class `Streamer` that supports streaming music albums (like Spotify). We later decide to also support playing records with a class `Turntable`. `Streamer` and `Turntable` have very similar functionality, however, they have incompatible interfaces (`search_album()` vs. `pick_record()`, `play_album()` vs. `play_record()`), so we have to call their specific methods instead of just reusing the existing interface. 

We could modify the `Turntable` class to be compatible with `Streamer` (e.g., by changing the name of the method `pick_record()` to `search_album()`, and `play_record()` to `play_album()`), but doing this could break some existing functionality and is hard to maintain. We may not even have this possibility, as `Turntable` could belong to a third-party library that we cannot change.

```python
# Application code

class Album:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

class Streamer:
    def __init__(self, catalog):
        self.catalog = catalog

    def search_album(self, title):
        for album in self.catalog:
            if album.title == title:
                return album

    def play_album(self, album):
        print(f"Streaming album {album.title} ({album.year}) by {album.artist}")

class Turntable:
    def __init__(self, catalog):
        self.catalog = catalog

    def pick_record(self, title):  # Should be renamed to "search_album" to be compatible with Streamer
        for album in self.catalog:
            if album.title == title:
                return album

    def play_record(self, album):  # Should be renamed to "play_album" to be compatible with Streamer
        print(f"Playing record {album.title} ({album.year}) by {album.artist}")
```

```python
# Client code

catalog = [
    Album("Autobahn", "Kraftwerk", 1974),
    Album("Violator", "Depeche Mode", 1990),
    Album("Homogenic", "Björk", 1997)
]

music_player = Streamer(catalog)
album = music_player.search_album("Autobahn")
music_player.play_album(album)

music_player = Turntable(catalog)
album = music_player.pick_record("Autobahn")
music_player.play_record(album)
```

### After

This issue is very easy to solve by using the `Adapter` pattern. We simply have to create a class `TurntableAdapter` that has methods with the same names as those for `Streamer`, and that are basically mappers to the `Turntable` methods.

Notice how this approach respects the **Single Responsibility Principle**, as we separate the interface conversion code in its own class, as well the **Open/Closed Principle**, since we can introduce new types of adapters without changing the existing code.

```python
# Application code

class TurntableAdapter:
    def __init__(self, turntable):
        self.turntable = turntable

    def search_album(self, title):
        album = self.turntable.pick_record(title)
        return album

    def play_album(self, album):
        self.turntable.play_record(album)
```

```python
# Client code

music_player = TurntableAdapter(Turntable(catalog))
album = music_player.search_album("Autobahn")
music_player.play_album(album)
```
