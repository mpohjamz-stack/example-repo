class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# Create albums1 with five Album objects
albums1 = [
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("The Dark Side of the Moon", 9, "Pink Floyd"),
    Album("Abbey Road", 17, "The Beatles"),
    Album("Hotel California", 9, "Eagles")
]

print("albums1:")
for album in albums1:
    print(album)

# Sort albums1 by number_of_songs
albums1.sort(key=lambda x: x.number_of_songs)
print("\nalbums1 sorted by number_of_songs:")
for album in albums1:
    print(album)

# Swap elements at index 0 and 1
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nalbums1 after swapping index 0 and 1:")
for album in albums1:
    print(album)

# Create albums2 with five Album objects
albums2 = [
    Album("Led Zeppelin IV", 8, "Led Zeppelin"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("Nevermind", 12, "Nirvana"),
    Album("The Wall", 26, "Pink Floyd"),
    Album("Born to Run", 8, "Bruce Springsteen")
]

print("\nalbums2:")
for album in albums2:
    print(album)

# Copy all albums from albums1 into albums2
albums2.extend(albums1)

# Add the two specified albums
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops! ... I Did It Again", 16, "Britney Spears"))

# Sort albums2 alphabetically by album name
albums2.sort(key=lambda x: x.album_name)
print("\nalbums2 sorted alphabetically by album name:")
for album in albums2:
    print(album)

# Search for "Dark Side of the Moon" and print its index
for i, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(f"\nIndex of 'Dark Side of the Moon' in albums2: {i}")
        break
