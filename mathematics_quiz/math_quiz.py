import random

def RandomInteger(minimum_value, maximum_value):
    """
    Generate a random integer within a specified range.

    Args:
        minimum_value (int): The minimum value of the range.
        maximum_value (int): The maximum value of the range.

    Returns:
        int: A random integer between minimum_value and maximum_value (inclusive).

    Raises:
        ValueError: If minimum_value or maximum_value is not an integer or if minimum_value > maximum_value.
    """
    try: 
        # Check if both inputs are integers and generate a random integer within the specified range
        if int(minimum_value) and int(maximum_value):
            return random.randint(minimum_value, maximum_value)
    except Exception as error:
        # Error message if inputs are not integers or if minimum_value > maximum_value
        print(f"\nValue should always be an Integer and Minimum Value <= Maximum Value, Minimum Value is {type(minimum_value).__name__} \
        and Maximum Value is {type(maximum_value).__name__}")
        raise ValueError

def RandomOperation():
    """
    Select a random arithmetic operation.

    Returns:
        str: A random arithmetic operation as a string ('+', '-', or '*').
    """
    # Randomly choose an operation from the list
    return random.choice(['+', '-', '*'])

def CalculateOperation(value1, value2, operation):
    """
    Perform an arithmetic operation on two values.

    Args:
        value1 (int): The first operand.
        value2 (int): The second operand.
        operation (str): The operation to perform ('+', '-', or '*').

    Returns:
        tuple: A tuple containing:
            - ProcessString (str): The formatted operation as a string.
            - Result (int): The result of the operation.
    """
    # Create a string representation of the operation for display
    ProcessString = f"{value1} {operation} {value2}"
    
    # Perform the correct operation based on the operator
    if operation == '+':
        Result = value1 + value2
    elif operation == '-': 
        Result = value1 - value2
    else: 
        Result = value1 * value2
    
    return ProcessString, Result

def math_quiz():
    """
    Run a math quiz game with 5 random arithmetic questions.

    The game will present the user with 5 arithmetic questions involving random integers and 
    operations. The user's score is displayed at the end.

    Raises:
        IOError: If the user enters a non-integer answer.
        Exception: If an error occurs during the game.
    """
    Points = 0   # Initialize points counter
    TotalQuestions = 5  # Set the number of questions in the quiz

    print("Welcome to the Math Quiz Game")
    print("You will be presented with 5 math problems, and you need to provide the correct answers.")

    try:
        # Loop through each question in the quiz
        for _ in range(TotalQuestions):
            # Generate two random integers and a random operation
            value_1 = RandomInteger(1, 10) 
            value_2 = RandomInteger(-10, -1)
            operation = RandomOperation()

            # Calculate the solution for the generated question
            Problem, Solution = CalculateOperation(value_1, value_2, operation)
            print(f"\nQuestion: {Problem}")
            try:
                # Get user input and ensure it's an integer
                useranswer = input("Your answer: ")
                useranswer = int(useranswer)
            except Exception as error:
                # Error message if user input is not an integer
                print("\n** Value should be an Integer **")
                raise IOError

            # Check if the user's answer matches the solution
            if useranswer == Solution:
                print("\nCorrect! You earned a point.")
                Points += 1  # Increment points if answer is correct
            else:
                print(f"\nWrong answer. The correct answer is {Solution}.")

        # Display final score after all questions
        print(f"\nGame over. Your score is: {Points}/{TotalQuestions}")
    except Exception as error:
        # Message if an exception occurs during the game
        print("\n** You are Terminated **")

if __name__ == "__main__":
    math_quiz()
