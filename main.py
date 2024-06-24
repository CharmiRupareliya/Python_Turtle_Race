import turtle  # Import the turtle module for creating graphics
import time
import random
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)   # Initialize colorama with auto-reset to avoid manual resets after each print

# Constants
WIDTH, HEIGHT = 500, 500 # Set the width and height of the turtle graphics window
COLORS = ['blue', 'black', 'pink', 'cyan', 'brown', 'purple', 'yellow', 'red', 'green', 'orange'] # List of colors for the turtles

#Function that Get the number of racers from the user.
def get_number_of_racers():
    racers = 0

    while True:
        racers = input(Style.BRIGHT + "Enter the number of Racers (2 - 10) : ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print(Fore.RED + "Please Enter Numeric Number.....")
            print()
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print(Fore.RED + "Number not in range of 2-10. Try again...... ")
            print()

#Function that Run the race until one of the turtles reaches the finish line.
def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20) # Generate a random distance for the turtle to move
            racer.forward(distance)   # Move the turtle forward by the random distance
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:   # Check if the turtle's y-coordinate has reached or exceeded the finish line
                return colors[turtles.index(racer)]

#Function that Create and initialize turtle racers based on given colors.
def create_turtles(colors):
    turtles = [] # Initialize an empty list to store turtle objects
    spacingx = WIDTH // (len(colors) + 1) # Calculate horizontal spacing between turtles
    for  i, color in enumerate(colors):
        racer = turtle.Turtle()   # Create a new turtle object
        racer.color(color)  # Set the turtle's color
        racer.shape('turtle')    # Set the turtle's shape to 'turtle'
        racer.left(90)   # Rotate the turtle to face upwards
        racer.penup()   # Lift the pen to avoid drawing lines while moving to the start position
        racer.setpos(-WIDTH // 2 +(i+1) * spacingx, -HEIGHT//2 +20)  # Set the turtle's position on the screen
        racer.pendown()   # Lower the pen to start drawing lines when moving
        turtles.append(racer)

    return turtles
def init_turtle():
    screen = turtle.Screen()  # Create a new screen object for the turtle graphics
    screen.setup(WIDTH, HEIGHT)  # Set the size of the turtle graphics window
    screen.title("Turtle Racing!!")   # Set the title of the turtle graphics window

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)  # Shuffle the list of colors to randomize turtle colors
colors = COLORS[:racers]   # Select the colors for the number of racers

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(6) #Give the user some time to see the result

