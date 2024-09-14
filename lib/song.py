class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name='99 Problems', artist='Jay Z', genre='Rap'):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
        if artist not in cls.artist_count:
                cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1

    @classmethod
    def get_genres(cls):
        return  cls.genres
    
    @classmethod
    def get_artists(cls):
        return cls.artists