import random

class Player:
    def __init__(self):
        self.__guess = None

    def make_guess(self):
        try:
            self.__guess = int(input('Now please enter a number between 1 to 50: '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.make_guess()

    def get_guess(self):
        return self.__guess


class Game:
    def __init__(self):
        self.number = random.randint(1, 51)

    def check_guess(self, player: Player):
        guess = player.get_guess()
        if guess == self.number:
            print(' You guessed the correct answer!')
            return True
        elif guess > self.number:
            print('Your guess is too high.')
        else:
            print('Your guess is too low.')
        return False


def main():
    print('Welcome to the Guess the Number game ')
    print('You have 5 chances to guess a number between 1 and 50.')

    game = Game()
    player = Player()

    for i in range(5):
        print(f"\nAttempt {i+1}/5")
        player.make_guess()
        if game.check_guess(player):
            break
    else:
        print(" You've run out of attempts. Better luck next time!")


if __name__ == "__main__":
    main()
