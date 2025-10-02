import random

class LotteryGame:
    def __init__(self, name="Baste & Etsab Corporation 6/60 Lottery", min_num=1, max_num=60, draw_size=6):

        self.name = name
        self.min_num = min_num
        self.max_num = max_num
        self.draw_size = draw_size
        self.winning_numbers = set()
        self.player_numbers = set()
        self.prize = 0
        self.match_count = 0

    def generate_winning_numbers(self):
        self.winning_numbers = set(random.sample(range(self.min_num, self.max_num + 1), self.draw_size))

    def get_player_numbers(self):

        print(f"\n{self.name}")
        print(f"\nEnter your {self.draw_size} chosen numbers ({self.min_num} - {self.max_num}):")

        while len(self.player_numbers) < self.draw_size:
            try:
                prompt = f"Number {len(self.player_numbers) + 1}: "
                num = int(input(prompt))

                # Input validation
                if not (self.min_num <= num <= self.max_num):
                    print(f"Number must be between {self.min_num} and {self.max_num}.")
                elif num in self.player_numbers:
                    print("You already picked this number. Try again.")
                else:
                    self.player_numbers.add(num)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_result(self):
        matches = self.winning_numbers.intersection(self.player_numbers)
        self.match_count = len(matches)

        # Simple prize logic: ₱1,000,000 for 6 matches, otherwise $1,000 per match
        if self.match_count == self.draw_size:
            self.prize = 1_000_000
        else:
            self.prize = self.match_count * 1000

    def display_result(self):
        matches = self.winning_numbers.intersection(self.player_numbers)

        print("\n--- LOTTERY RESULT ---")
        print("Winning Numbers :", sorted(self.winning_numbers))
        print("Your Numbers    :", sorted(self.player_numbers))
        print("Matched Numbers :", sorted(matches) if matches else "None")
        print("Total Matches   :", self.match_count)
        print(f"Prize           : ₱{self.prize:,}")

    def play(self):

        self.generate_winning_numbers()
        self.get_player_numbers()
        self.calculate_result()
        self.display_result()


if __name__ == "__main__":
    game = LotteryGame()
    game.play()