import random

def main():
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        """
        
        # TODO: Ask the user for their name using input()
        name = input("Enter your name: ")

        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        player = {"name": name, "health": 10, "inventory": []}

        # TODO: Return the dictionary
        return player


    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.
        """
        # TODO: Create a dictionary of treasure names and integer values
        treasures = {
            "gold coin": 5,
            "ruby": 10,
            "ancient scroll": 7,
            "emerald": 9,
            "silver ring": 4
        }

        # TODO: Return the dictionary
        return treasures


    def create_traps():
        """
        Creates a dictionary of traps with varying damage levels.

        Returns:
            dict: Example:
                {
                    "spike pit": 3,
                    "poison darts": 2,
                    "falling rocks": 4,
                    "swinging blade": 3,
                    "fire blast": 5
                }
        """
        # TODO: Create a dictionary of trap names and integer damage values
        traps = {
            "spike pit": 3,
            "poison darts": 2,
            "falling rocks": 4,
            "swinging blade": 3,
            "fire blast": 5
        }

        # TODO: Return the dictionary
        return traps


    def display_options(room_number):
        """
        Displays available options for the player in the current room.
        """
        # TODO: Print the room number and the 4 menu options listed above
        print(f"\nYou are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search for treasure")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")


    def search_room(player, treasures, traps):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses health based on trap damage.
        """

        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        outcome = random.choice(["treasure", "trap"])

        # TODO: Write an if/else to handle treasure vs trap outcomes
        if outcome == "treasure":

            # TODO: Choose a random treasure from the treasures dictionary
            treasure = random.choice(list(treasures.keys()))

            # TODO: Add the treasure to the player's inventory
            player["inventory"].append(treasure)

            # TODO: Print a message describing what was found
            print(f"You found a {treasure}!")

        else:

            # TODO: Choose a random trap from the traps dictionary
            trap = random.choice(list(traps.keys()))

            # TODO: Subtract the trap's damage from the player's health
            damage = traps[trap]
            player["health"] -= damage

            # TODO: Print a warning message
            print(f"You triggered a {trap}! You lost {damage} health points.")

        # TODO: Update player dictionary accordingly
        player.update({
            "health": player["health"],
            "inventory": player["inventory"]
        })

        # TODO: Print messages describing what happened and the player's new health or inventory status
        print(f"Your health is now {player['health']}")
        print(f"Your inventory contains: {', '.join(player['inventory']) if player['inventory'] else 'You have no items yet.'}")


    def check_status(player):
        """
        Displays the player’s current health and inventory.
        """
        # TODO: Print player health
        print(f"Health: {player['health']}")

        # TODO: If the inventory list is not empty, print items joined by commas
        if player["inventory"]:
            print(f"Inventory: {', '.join(player['inventory'])}")

        # TODO: Otherwise print “You have no items yet.”
        else:
            print("Inventory: You have no items yet.")


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        total_score = sum(treasures[item] for item in player["inventory"])

        # TODO: Print final health, items, and total value
        print(f"\nFinal Health: {player['health']}")
        print(f"Final Inventory: {', '.join(player['inventory']) if player['inventory'] else 'You have no items yet.'}")
        print(f"Total Score: {total_score}")

        # TODO: End with a message like "Game Over! Thanks for playing."
        print("Game Over! Thanks for playing.")


    def run_game_loop(player, treasures, traps):
        """
        Main game loop that manages the rooms and player decisions.

        Flow:
            - There are 5 rooms
            - Player can search, move, check status, or quit
        """

        # TODO: Loop through 5 rooms (1–5)
        for room_number in range(1, 6):

            while True:

                display_options(room_number)

                # TODO: Inside each room, prompt player choice using input()
                choice = input("Enter your choice (1-4): ")

                # TODO: Use if/elif to handle each choice (1–4)
                if choice == "1":

                    search_room(player, treasures, traps)

                    if player["health"] < 1:
                        print("You have died from your injuries!")
                        end_game(player, treasures)
                        return

                elif choice == "2":
                    print("You move to the next room.")
                    break

                elif choice == "3":
                    check_status(player)

                elif choice == "4":
                    print("You have chosen to quit the game.")
                    end_game(player, treasures)
                    return

                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

        # TODO: Break or return appropriately when player quits or dies

        # TODO: Call end_game() after all rooms are explored
        end_game(player, treasures)


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    traps = create_traps()
    run_game_loop(player, treasures, traps)


if __name__ == "__main__":
    main()
