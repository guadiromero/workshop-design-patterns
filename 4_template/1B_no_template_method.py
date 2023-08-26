"""
An implementation without using any Design Patterns,
with a class for each algorithm.
"""
class ClassicMate:
    def make_mate(self):
        # Get ingredients
        print("Get yerba and 1/5 liter of water.\n")  # Customized step

        # Prepare water
        print("Heat water to 80 degrees Celsius.\n")

        # Fill with yerba
        print("Fill 3/4 of the mate cup with yerba.\n")

        # Pour water
        print("Pour a bit of water and drink.\n")

        # Enjoy
        print("*Ruidito de mate*")


class MateCordooobes:
    def make_mate(self):
        # Get ingredients
        print("Get yerba, 1/5 liter of water and herbs.\n")  # Customized step

        # Prepare water
        print("Heat water to 80 degrees Celsius.\n")

        # Fill with yerba
        print("Fill 3/4 of the mate cup with yerba.\n")

        # Add herbs
        print("Put some herbs inside of the mate cup.\n")  # Extra step

        # Pour water
        print("Pour a bit of water and drink.\n")

        # Enjoy
        print("*Ruidito de mate*")


class Terere:
    def make_mate(self):
        # Get ingredients
        print("Get yerba, 3 grapefruits and ice cubes.\n")  # Customized step

        # Prepare water
        print("Squeeze the grapefruits and add the ice cubes to the juice.\n")

        # Fill with yerba
        print("Fill 3/4 of the mate cup with yerba.\n")

        # Pour water
        print("Pour a bit of water and drink.\n")

        # Enjoy
        print("*Ruidito de mate*")


# Client code
MateCordooobes().make_mate()
