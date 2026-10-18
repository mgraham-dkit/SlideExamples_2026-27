from d_composition.music import MusicPlayer, Song

my_zune = MusicPlayer("Michelle Graham")
my_zune.play_random_song()

song1 = Song("Wildest Dreams", "Taylor Swift")
song2 = Song("Style", "Taylor Swift")
song3 = Song("Father Figure", "Taylor Swift")
song4 = Song("Tolerate It", "Taylor Swift")
song5 = Song("Patient Zero", "Taylor Swift")
library = [song1, song2, song3, song4, song5]

backup_zune = MusicPlayer("Also Michelle Graham", library)
backup_zune.play_random_song()

my_zune.add(song5)
my_zune.add(song4)

overlap = backup_zune.get_shared_songs(my_zune)
if overlap:
    print("Our tastes overlap - we both have:")
    for song in overlap:
        print(f"\t{song.title} by {song.artist}")