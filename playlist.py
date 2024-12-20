import random
import pygame

# Dictionary mapping emotions to playlists
playlists = {
    'Happy': ['music/happy_song1.mp3', 'music/happy_song2.mp3'],
    'Sad': ['music/sad_song1.mp3', 'music/sad_song2.mp3'],
    'Angry': ['music/angry_song1.mp3', 'music/angry_song2.mp3'],
    # Add more categories as needed
}

def play_music(emotion):
    pygame.mixer.init()
    if emotion in playlists:
        song = random.choice(playlists[emotion])
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

if __name__ == "__main__":
    play_music('Happy')  # Example call
