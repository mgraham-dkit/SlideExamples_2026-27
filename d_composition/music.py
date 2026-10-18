from __future__ import annotations
import random as rand


class Song:
    count: int = 0

    def __init__(self, title: str, artist: str):
        Song.count+=1

        self.song_id = Song.count

        self.title = title
        self.artist = artist


class MusicPlayer:
    count: int = 0

    def __init__(self, owner:str, library: list[Song] | None = None):
        self.owner = owner

        MusicPlayer.count += 1
        self.id = MusicPlayer.count

        if library is None:
            library = []

        self.library = library

    def display(self) -> None:
        print(f"{self.__class__.__name__}[Count={MusicPlayer.count}, id={self.id}, owner={self.owner}, library={self.library}]")

    def search_library(self, target_song: Song) -> bool:
        song_title = target_song.title.lower()
        song_artist = target_song.artist.lower()

        for current_song in self.library:
            if current_song.title.lower() == song_title and current_song.artist.lower() == song_artist:
                return True

        return False

    def add(self, song: Song) -> bool:
        if not self.search_library(song):
            self.library.append(song)
            return True

        return False

    def display_library(self):
        for song in self.library:
            print(f"{song.title} by {song.artist}")

    def get_random_song(self) -> Song | None:
        if not self.library:
            return None

        index = rand.randint(0, len(self.library)-1)
        return self.library[index]

    def play_random_song(self) -> None:
        # Get a randomly selected song
        song = self.get_random_song()

        # If a real song was returned (i.e. the library is not empty)
        if not song:
            # Display a message to the user
            print("Library is empty. Please add some songs!")
        else:
            # Otherwise, play the song
            print(f"Now playing {song.title} by {song.artist}!")

    def get_shared_songs(self, other_player: MusicPlayer) -> list[Song]:
        overlapping = []
        for song in self.library:
            if other_player.search_library(song):
                overlapping.append(song)

        return overlapping