import random
import pygame
playlists = {
    'Happy': ['happy_song1.mp3', 'happy_song2.mp3'],
    'Sad': ['sad_song1.mp3', 'sad_song2.mp3'],
    'Angry': ['angry_song1.mp3', 'angry_song2.mp3'],
    
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
    play_music('Happy')  
