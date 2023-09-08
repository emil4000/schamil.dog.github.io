import streamlit as st
import datetime
import time
import threading
import pygame
from PIL import Image
from io import BytesIO

# Streamlit App
st.title("Hunde-Spaziergangsprogramm")
st.subheader("Video abspielen")
video_file = open("baby_dog15.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
# Eingabefelder für Uhrzeit und Dauer
st.subheader("Spaziergang planen")
hour = st.number_input("Stunde:", min_value=0, max_value=23)
minute = st.number_input("Minute:", min_value=0, max_value=59)
duration = st.number_input("Dauer (in Minuten):", min_value=1)

# Start- und Stop-Ton auswählen
st.subheader("Töne auswählen")
selected_start_sound_file = st.file_uploader("Start-Ton wählen (mp3, wav)", type=["mp3", "wav"])
selected_stop_sound_file = st.file_uploader("Stop-Ton wählen (mp3, wav)", type=["mp3", "wav"])

# Bild auswählen
st.subheader("Bild auswählen")
dog_images = [
    Image.open("Hundebild1.jpg"),
    Image.open("Hundebild2.jpg"),
    Image.open("Hundebild3.jpg")
]
selected_image_index = st.number_input("Bild wählen:", min_value=0, max_value=len(dog_images) - 1, step=1)
st.image(dog_images[selected_image_index], use_column_width=True)

# Funktion zum Starten des Spaziergangs
def start_walk():
    current_time = datetime.datetime.now().time()
    walk_time = datetime.time(hour, minute)
    walk_duration = duration * 60
    if current_time >= walk_time:
        start_delay = datetime.datetime.combine(datetime.date.today(), walk_time) + datetime.timedelta(days=1) - datetime.datetime.now()
    else:
        start_delay = datetime.datetime.combine(datetime.date.today(), walk_time) - datetime.datetime.now()
    threading.Timer(start_delay.total_seconds(), walk_dogs, args=(walk_duration, selected_start_sound_file, selected_stop_sound_file)).start()

# Funktion zum Spazierengehen der Hunde
def walk_dogs(duration, start_sound, stop_sound):
    pygame.mixer.init()
    pygame.mixer.music.load(start_sound)
    pygame.mixer.music.play()
    st.write("Starte den Spaziergang mit den Hunden...")
    time.sleep(duration)
    pygame.mixer.music.load(stop_sound)
    pygame.mixer.music.play()
    st.write("Spaziergang beendet!")

# Button "Spaziergang starten"
start_walk_button = st.button("Spaziergang starten", on_click=start_walk)

# Streamlit App starten
if __name__ == "__main__":
    pygame.init()  # Pygame initialisieren (wird benötigt, um Sounds abzuspielen)
    st.set_page_config(layout="wide")

