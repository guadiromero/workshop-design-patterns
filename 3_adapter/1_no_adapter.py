"""
An implementation without using any Design Patterns.
"""
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


# Client code
catalog = [
    Album("Autobahn", "Kraftwerk", 1974),
    Album("Violator", "Depeche Mode", 1990),
    Album("Homogenic", "Björk", 1997)
]

streamer = Streamer(catalog)
album = streamer.search_album("Autobahn")
streamer.play_album(album)

turntable = Turntable(catalog)
album = turntable.pick_record("Autobahn")
turntable.play_record(album)
