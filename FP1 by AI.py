import random

def generate_and_display_numbers():
    """
    Asks the user for their name, greets them, and generates six random
    numbers with specific spacing.
    """
    # 1. Ask for the user's name and store it in the specified variable
    varUserName = input("Hello! What is your name? ")

    # 2. Greet the user by their name
    print(f"Nice to meet you, {varUserName}!")
    print("Generating your random numbers...")

    # 3. Generate six random numbers using the randint function
    # The range is 1 to 100, which is a common range for this type of program.
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    number3 = random.randint(1, 100)
    number4 = random.randint(1, 100)
    number5 = random.randint(1, 100)
    number6 = random.randint(1, 100)

    # 4. Print the numbers with the specific spacing requirements
    #    - Two spaces between the first five numbers
    #    - Four spaces between the fifth and sixth number
    print(f"{number1}  {number2}  {number3}  {number4}  {number5}    {number6}")

    # 5. Farewell message for the user
    print("Hope you have a great day!")

# Call the main function to run the script
if __name__ == "__main__":
    generate_and_display_numbers()