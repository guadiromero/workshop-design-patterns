"""
An implementation using conditional statements.
"""
class ClothesCleaner:
    def clean(self, stain):
        # Remove stains
        if stain == "coffee":
            print("Apply baking soda and a bit of water to the stain. Scrub for some minutes.")
        elif stain == "wine":
            print("Put some salt on the stain. Wait for five minutes.")

        # Proceed with washing cycle
        print("Wash clothes as usual.")


# Client code
clothes_cleaner = ClothesCleaner()
clothes_cleaner.clean("wine")
