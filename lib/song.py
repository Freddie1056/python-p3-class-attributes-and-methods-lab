class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment song count
        Song.add_song_to_count()

        # Add genre and artist
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

        # Update genre and artist counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add genre to genres list if not already present
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add artist to artists list if not already present
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increment the count for the genre in genre_count dictionary
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Increment the count for the artist in artist_count dictionary
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
thunderstruck = Song("Thunderstruck", "AC/DC", "Rock")
god_bless_texas = Song("God Bless Texas", "Little Texas", "Country")
another_rap_song = Song("Another Rap Song", "Jay-Z", "Rap")

# Testing the class attributes:
print(Song.count)  # Output: 4
print(Song.genres)  # Output: ['Rap', 'Rock', 'Country']
print(Song.artists)  # Output: ['Jay-Z', 'AC/DC', 'Little Texas']
print(Song.genre_count)  # Output: {'Rap': 2, 'Rock': 1, 'Country': 1}
print(Song.artist_count)  # Output: {'Jay-Z': 2, 'AC/DC': 1, 'Little Texas': 1}

