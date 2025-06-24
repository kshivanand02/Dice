import random
import time
import sys

def rolling_animation():
    animation = ["Rolling", "Rolling.", "Rolling..", "Rolling..."]
    for frame in animation:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.5)
    print()

def roll_dice():
    input("🎲 Press Enter to roll the die...")
    rolling_animation()
    result = random.randint(1, 6)
    print(f"\n🎯 You rolled a {result}!\n")

# Main loop
if __name__ == "__main__":
    while True:
        roll_dice()
        again = input("🔁 Roll again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break
