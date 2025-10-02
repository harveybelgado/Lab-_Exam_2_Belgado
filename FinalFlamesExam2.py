class FlamesCalculator:

    def __init__(self, outcomes=None):
        if outcomes is None:
            self.outcomes = {
                "F": "Friendship",
                "L": "Love",
                "A": "Affection",
                "M": "Marriage",
                "E": "Enemy",
                "S": "Sibling"
            }
        else:
            self.outcomes = outcomes

        self.name1 = ""
        self.name2 = ""
        self.result = None

    def get_names(self):
        print('FLAMES SYSTEM')
        self.name1 = input("Enter first name: ")
        self.name2 = input("Enter second name: ")

    def calculate(self):
        n1 = list(self.name1.replace(" ", "").upper())
        n2 = list(self.name2.replace(" ", "").upper())

        for letter in n1[:]:  # Iterate over a copy of n1
            if letter in n2:
                n1.remove(letter)
                n2.remove(letter)

        remains = len(n1) + len(n2)

        if remains == 0:
            self.result = 'Not compatible! Single forever </3'
            return

        flames_str = "FLAMES"
        flames_key = flames_str[(remains - 1) % len(flames_str)]

        self.result = self.outcomes.get(flames_key)

    def display_result(self):
        """
        Prints the final FLAMES result.
        """
        if self.result:
            print("Result:", self.result)
        else:
            print("Not compatible! Single forever </3")

    def run(self):
  
        self.get_names()
        self.calculate()
        self.display_result()

if __name__ == "__main__":
    flames_game = FlamesCalc()

    flames_game.run()
