import pyautogui
import time
import random
import sys

# Function to read words from a local text file with specified encoding
def read_words_from_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            words = file.readlines()
            return [word.strip() for word in words]
    except FileNotFoundError:
        print("File not found.")
        return []
    except UnicodeDecodeError:
        print("Error decoding the file. Try a different encoding.")
        return []

# Path to your local text file
file_path = r"C:\Users\Ariful\Downloads\animals.txt"  # Use 'r' before the string to indicate a raw string

# Read words from the local text file
words = read_words_from_file(file_path)

if words:
    time.sleep(4)  # Wait for 4 seconds before starting
    while True:
        try:
            # Choose a random word from the list of words
            random_word = random.choice(words)

            # Construct the phrase
            phrase = "You are  a " + random_word

            # Typing the phrase
            pyautogui.typewrite(phrase)
            pyautogui.press("enter")

            # Random delay to mimic human behavior
            time.sleep(random.uniform(1, 2))  # Sleep between 1 and 2 seconds
        except pyautogui.FailSafeException:
            print("Mouse moved to a corner of the screen. Exiting...")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)
else:
    print("No words found in the file. Exiting the program.")
