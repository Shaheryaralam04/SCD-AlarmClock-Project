import streamlit as st
from time import strftime
import datetime
import time
import pygame

st.set_page_config(page_title="Digital Clock by For SCD Project", page_icon="🕰️", layout="wide")

# Digital Clock
def clock():
    string = strftime("%H:%M:%S")
    month = strftime("%B")
    month1 = strftime("%m")
    year = strftime("%Y")
    day = strftime("%A")

    st.write(f"# {string}")
    st.write(f"{month} {month1} {year} | {day}")
    time.sleep(1)

# Alarm
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        st.write(now)
        if now == set_alarm_timer:
            st.write("Time to Wake up")
            pygame.mixer.music.load("Alarm-ringtone.mp3")
            pygame.mixer.music.play()
            break

# Streamlit UI
st.title("Digital Clock by For SCD Project")
st.markdown("---")

# Clock
while True:
    clock()

    # Alarm
    if st.button("Set Alarm"):
        set_alarm_timer = st.time_input("Set the alarm time", value=datetime.datetime.now().strftime("%H:%M"))
        alarm(set_alarm_timer.strftime("%H:%M:%S"))

    if st.button("Stop Alarm"):
        pygame.mixer.music.stop()
