import random

def main():

    def setup_player():
        """
        Prompts the user to create their player profile.
        """
        # TODO: Ask the user for their name using input()
        name = input("Enter your name: ")

        # TODO: Initialize a dictionary with keys: name, health, inventory, potions
        player = {
            "name": name,
            "health": 10,
            "inventory": [],
            "potions": 2
        }

        # TODO: Return the dictionary
        return player


    def create_treasures():
        """
        Creates a dictionary of treasures and their values.
        """
        treasures = {
            "gold coin": 5,
            "ruby": 10,
            "ancient scroll": 7,
            "emerald": 9,
            "silver ring": 4
        }

        return treasures


    def create_traps():
        """
        Creates a dictionary of traps and damage values.
        """
        traps = {
            "spike trap": 3,
            "poison darts": 2,
            "falling rocks": 4,
            "hidden pit": 5
        }

        return traps


    def display_options(room_number):
        """
        Displays available options for the player in the current room.
        """
        print(f"\nYou are in room {room_number}.")
        print("What would you like to do?")
        print("1. Search the room")
        print("2. Move to next room")
        print("3. Check health and inventory")
        print("4. Quit the game")


    def search_room(player, treasures, traps):
        """
        Simulates searching the room for treasure, traps, or potions.
        """

        outcome = random.choice(["treasure", "trap", "potion"])

        if outcome == "treasure":

            treasure = random.choice(list(treasures.keys()))
            player["inventory"].append(treasure)

            print(f"You found a {treasure}!")

        elif outcome == "trap":

            trap = random.choice(list(traps.keys()))
            damage = traps[trap]

            player["health"] -= damage

            print(f"You triggered a {trap}! You lost {damage} health.")

        elif outcome == "potion":

            player["potions"] += 1
            print("You found a healing potion!")

        print(f"Current Health: {player['health']}")
        print(f"Potions: {player['potions']}")


    def check_status(player):
        """
        Displays player health and inventory.
        Allows potion usage.
        """

        print(f"\nHealth: {player['health']}")
        print(f"Potions: {player['potions']}")

        if player["inventory"]:
            print("Inventory:", ", ".join(player["inventory"]))
        else:
            print("Inventory: You have no items yet.")

        if player["potions"] > 0:
            use = input("Would you like to use a healing potion? (y/n): ")

            if use.lower() == "y":
                player["health"] += 5
                player["potions"] -= 1

                # Prevent health exceeding max
                if player["health"] > 10:
                    player["health"] = 10

                print("You used a potion and restored 5 health!")


    def end_game(player, treasures):
        """
        Ends the game and displays final results.
        """

        total_value = sum(treasures[item] for item in player["inventory"] if item in treasures)

        print("\n===== GAME SUMMARY =====")
        print(f"Player: {player['name']}")
        print(f"Final Health: {player['health']}")

        if player["inventory"]:
            print("Treasures Collected:", ", ".join(player["inventory"]))
        else:
            print("Treasures Collected: None")

        print(f"Total Treasure Value: {total_value}")
        print("Game Over! Thanks for playing.")


    def run_game_loop(player, treasures, traps):
        """
        Main game loop.
        """

        for room_number in range(1, 6):

            while True:

                display_options(room_number)

                choice = input("Enter your choice (1-4): ")

                if choice == "1":

                    search_room(player, treasures, traps)

                    if player["health"] <= 0:
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
                    print("Invalid choice. Please choose 1-4.")

        end_game(player, treasures)


    # -----------------------------
    # GAME ENTRY POINT
    # -----------------------------
    player = setup_player()
    treasures = create_treasures()
    traps = create_traps()

    run_game_loop(player, treasures, traps)


if __name__ == "__main__":
    main()