# Save this code in a file named add_0.py

# Define the add function
def add(a, b):
    return a + b

# Check if the script is being run directly
if __name__ == "__main__":
    # Assign values to variables
    a = 1
    b = 2

    # Print the result using string format
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
