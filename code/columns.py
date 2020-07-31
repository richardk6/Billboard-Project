class Unemploy_Cols:
    year = "Year"
    month = "Month"
    rate = "Unemployment Rate"
    
class Music_Cols:
    track = "Track"
    artist = "Artist"
    placement = "Placement"
    year = "Year"
    month = "Month"
    day = "Day"
    danceability = "danceability"
    energy = "energy"
    key = "key"
    loudness = "loudness"
    speechiness = "speechiness"
    acousticness = "acousticness"
    liveness = "liveness"
    valence = "valence"
    tempo = "tempo"

class Music_Unemploy_Cols:
    track = Music_Cols.track
    artist = Music_Cols.artist
    placement = Music_Cols.placement
    year = Music_Cols.year
    month = Music_Cols.month
    day = Music_Cols.day
    danceability = Music_Cols.danceability
    energy = Music_Cols.energy
    key = Music_Cols.key
    loudness = Music_Cols.loudness
    speechiness = Music_Cols.speechiness
    acousticness = Music_Cols.acousticness
    liveness = Music_Cols.liveness
    valence = Music_Cols.valence
    tempo = Music_Cols.tempo
    unemploy_rate = Unemploy_Cols.rate


