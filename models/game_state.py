# Game state and rules

class Scoreboard:
    """
    A class to manage the scoreboard for a player in Generala.
    Keeps track of the combinations, their scores, and whether they have been played.
    """

    def __init__(self):
        # Initialize the scoreboard with all combinations and their played status
        self.combinations = {
            "Generala Doble": {"score": None, "played": False},
            "Generala": {"score": None, "played": False},
            "Pócker": {"score": None, "played": False},
            "Full": {"score": None, "played": False},
            "Escalera": {"score": None, "played": False},
            "Sixes": {"score": None, "played": False},
            "Fives": {"score": None, "played": False},
            "Fours": {"score": None, "played": False},
            "Threes": {"score": None, "played": False},
            "Twos": {"score": None, "played": False},
            "Ones": {"score": None, "played": False}
        }

    def add_score(self, combination, score):
        """
        Add the score for a specific combination and mark it as played.
        :param combination: The combination to add the score for.
        :param score: The points scored for the combination.
        """
        if combination not in self.combinations:
            raise ValueError(f"Invalid combination: {combination}")
        if self.combinations[combination]["played"]:
            raise ValueError(f"Combination {combination} has already been played.")

        self.combinations[combination]["score"] = score
        self.combinations[combination]["played"] = True

    def cross_out(self, combination):
        """
        Cross out a combination (mark it as played) with a score of zero points.
        :param combination: The combination to cross out.
        """
        if combination not in self.combinations:
            raise ValueError(f"Invalid combination: {combination}")
        if self.combinations[combination]["played"]:
            raise ValueError(f"Combination {combination} has already been played.")

        self.combinations[combination]["score"] = 0
        self.combinations[combination]["played"] = True

    def get_total_score(self):
        """
        Calculate the total score from all played combinations.
        :return: The total score as an integer.
        """
        return sum(score["score"] for score in self.combinations.values() if score["score"] is not None)

    def get_available_combinations(self):
        """
        Get a list of combinations that have not been played yet.
        :return: A list of available combinations.
        """
        return [comb for comb, details in self.combinations.items() if not details["played"]]

    def display_scoreboard(self):
        """
        Display the current scoreboard.
        """
        print("Scoreboard:")
        for combination, details in self.combinations.items():
            status = "Played" if details["played"] else "Available"
            score = details["score"] if details["score"] is not None else "-"
            print(f"{combination}: {score} ({status})")