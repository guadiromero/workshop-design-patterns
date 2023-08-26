"""
An implementation without using any Design Patterns,
with a monolithic algorithm.
"""
class Mate:
    def make_mate(self, type):
        # Get ingredients
        if type == "classic":
            print("Get yerba and 1/5 liter of water.\n")
        elif type == "cordobés":
            print("Get yerba, 1/5 liter of water and herbs.\n")
        elif type == "tereré":
            print("Get yerba, 3 grapefruits and ice cubes.\n")

        # Prepare water
        print("Heat water to 80 degrees Celsius.\n")

        # Fill with yerba
        print("Fill 3/4 of the mate cup with yerba.\n")

        # Add herbs
        if type == "cordobés":
            print("Put some herbs inside of the mate cup.\n")

        # Pour water
        print("Pour a bit of water and drink.\n")

        # Enjoy
        print("*Ruidito de mate*")


# Client code
Mate().make_mate("cordobés")
