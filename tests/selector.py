#Select & Print Random Trope
import random

file_path = './Tropes.txt'

def print_random_line():
    with open(file_path, 'r') as file:
        
        allTropes = file.readlines()  # Read all lines into a list
        
randomTrope = random.choice(allTropes).strip()  # Randomly select a line and strip newline

print(randomTrope)
