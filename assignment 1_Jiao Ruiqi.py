
# Name: [Jiao Ruiqi]
# Assignment One

import turtle

def task_1_turtle():
    print("\n--- Running Task 1: Turtle Drawing ---")
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Turtle Drawing - Dynamic Colorful Star")

    # Create a turtle
    t = turtle.Turtle()
    t.speed(10) # Set drawing speed
    t.width(2)

    # Define a list of colors
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    # Use structured for loops to draw beautiful colourful patterns
    # Drawing a spiral star with dynamically changing colors and lengths
    for i in range(36):
        # Dynamically change color
        t.color(colors[i % len(colors)])

        # Dynamically change length (increases each time to form a spiral effect)
        length = 100 + (i * 5)

        # Draw one point of the star
        t.forward(length)
        t.right(144) # Angle for a star shape

    print("Please view the drawing in the pop-up window.")
    print("Click anywhere on the window to exit the drawing mode.")
    screen.exitonclick()



def task_2_qa_bot():
    print("\n--- Running Task 2: QA Bot ---")
    print("Bot: Hello! I am a QA bot. You can ask me about the following keywords:")
    print("[HKU, robot, jetson, ai, human]")
    print("(Type 'exit' to end the conversation)")

    while True:
        # Use input() to receive questions
        question = input("\nYou: ").lower()

        # Exit condition
        if question == "exit":
            print("Bot: Goodbye! Looking forward to our next chat.")
            break

        # Use if / elif / else for conditional logic matching user queries
        # Supports at least 5 keywords
        if "hku" in question:
            print("Bot: HKU (The University of Hong Kong) is a top international public research university located in Hong Kong, known for its high academic reputation.")
        elif "jetson" in question:
            print("Bot: NVIDIA Jetson is an embedded computing platform often used for edge AI and robotics development, such as the Nano, Xavier, and Orin series.")
        elif "robot" in question:
            print("Bot: A robot is a machine that can automatically execute tasks. They can assist humans in dangerous, repetitive, or high-precision work.")
        elif "ai" in question or "artificial intelligence" in question:
            print("Bot: Artificial Intelligence (AI) is a branch of computer science dedicated to creating machines that can simulate human intelligence.")
        elif "human" in question:
            print("Bot: Humans are the most intelligent creatures on Earth, and also the creators of us robots!")
        else:
            print("Bot: Sorry, I haven't learned about this question yet. Please try to include the keywords mentioned above.")

# ==========================================
# Main Program Entry

if __name__ == "__main__":
    print("Assignment 1: Python Basics")
    print("Please select a task to run:")
    print("1. Turtle Drawing (Task A)")
    print("2. QA Bot (Task B)")

    choice = input("Enter option number (1/2): ")

    if choice == '1':
        task_1_turtle()
    elif choice == '2':
        task_2_qa_bot()
    else:
        print("Invalid input, program exiting.")