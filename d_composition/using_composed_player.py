# Import the class
from d_composition.music import MusicPlayer, Song

# Create a MusicPlayer with a default library
my_zune = MusicPlayer("Michelle Graham")
# Play a random song from my_zune - this will display a message saying
# to add songs as the default library is empty!
my_zune.play_random_song()

# Create a second music player and supply a library as well as owner info
# This version of the library stores Songs as objects, not just basic strings
song1 = Song("Wildest Dreams", "Taylor Swift")
song2 = Song("Style", "Taylor Swift")
song3 = Song("Father Figure", "Taylor Swift")
song4 = Song("Tolerate It", "Taylor Swift")
song5 = Song("Patient Zero", "Taylor Swift")
library = [song1, song2, song3, song4, song5]

backup_zune = MusicPlayer("Also Michelle Graham", library)
# Play a random song from the second player object (backup_zune) -
# this will display a message saying a random song is being played
backup_zune.play_random_song()

my_zune.add(song5)
my_zune.add(song1)

overlap = backup_zune.get_shared_songs(my_zune)
if overlap:
    print("Our tastes overlap - we both have:")
    for song in overlap:
        print(f"\t{song.title} by {song.artist}")