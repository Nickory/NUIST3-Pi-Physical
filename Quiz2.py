# Author: Ziheng
# Date: 2025.4.2
# Description: Interactive Quiz Game with LED feedback using Raspberry Pi GPIO

import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define LED pins
GREEN_LED = 17  # GPIO pin for correct answer LED
RED_LED = 18    # GPIO pin for incorrect answer LED

# Set up LED pins as outputs
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# Function to clean up GPIO at exit
def cleanup():
    GPIO.output(GREEN_LED, GPIO.LOW)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.cleanup()

# Function to flash LED
def flash_led(led_pin, duration=1):
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(led_pin, GPIO.LOW)

def quiz():
    try:
        print("Welcome to the Animal Quiz with LED feedback!")
        print("Answer the following questions:")

        # Questions and Answers
        questions = [
            "1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. Cat",
            "2. Which bird can fly backwards?: a. Cuckoo, b. Eagle, c. Hummingbird ",
            "3. What is the only mammal capable of flight?: a. Bat, b. Squirrel, c. Dolphin "
        ]
        answers = [
            "a",
            "c",
            "a"
        ]
        score = 0

        # Ask questions
        for i in range(len(questions)):
            user_answer = input(questions[i]).strip().lower()
            
            if user_answer == answers[i]:
                print("Correct!")
                flash_led(GREEN_LED)  # Flash green LED for correct answer
                score += 1
            else:
                print("Incorrect!")
                flash_led(RED_LED)    # Flash red LED for incorrect answer

        # Provide final score
        print("\nQuiz completed!")
        print(f"You got {score}/{len(questions)} questions correct.")
        
        # Flash both LEDs for quiz completion
        for _ in range(3):
            GPIO.output(GREEN_LED, GPIO.HIGH)
            GPIO.output(RED_LED, GPIO.HIGH)
            time.sleep(0.3)
            GPIO.output(GREEN_LED, GPIO.LOW)
            GPIO.output(RED_LED, GPIO.LOW)
            time.sleep(0.3)
            
    except KeyboardInterrupt:
        print("\nQuiz interrupted by user")
    finally:
        cleanup()

# Run the quiz function
if __name__ == "__main__":
    quiz()
