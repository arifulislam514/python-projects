import pyautogui
import time
import random

# Function to read words from a local text file
def read_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.readlines()
            return [word.strip() for word in words]
    except FileNotFoundError:
        print("File not found.")
        return []

# Path to your local text file
file_path = r"C:\Users\Ariful\Downloads\animals.txt"  # Use 'r' before the string to indicate a raw string

# Read words from the local text file
words = read_words_from_file(file_path)

if words:
    time.sleep(3)
    while True:
        # Choose a random word from the list of words
        random_word = random.choice(words)

        # Typing the random word
        pyautogui.typewrite(random_word, interval=0.1)  # Added interval for natural typing
        pyautogui.press("enter")
        time.sleep(1)  # Adjust the delay as needed
else:
    print("No words found in the file. Exiting the program.")

