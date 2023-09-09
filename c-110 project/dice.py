import random

class DiceSimulator:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

if __name__ == "__main__":
    dice = DiceSimulator()  

    while True:
        input("Press Enter to roll the dice...")
        result = dice.roll()
        print(f"You rolled: {result}")
        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            break
