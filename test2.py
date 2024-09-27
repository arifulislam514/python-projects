import pyautogui
import time
import random
import requests


# Function to fetch words from GitHub text file
def fetch_words():
    url = "https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54"
    response = requests.get(url)
    if response.status_code == 200:
        word = response.text.splitlines()
        return word
    else:
        print("Failed to fetch words from the URL.")
        return []


# Fetch words from the text file
words = fetch_words()

if words:
    time.sleep(4)
    while True:
        # Choose a random word from the list of words
        random_word = random.choice(words)

        # Typing the random word
        pyautogui.typewrite(random_word)
        pyautogui.press("enter")
        time.sleep(1)  # Adjust the delay as needed
else: