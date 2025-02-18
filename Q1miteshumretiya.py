def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False  # Changed "false" (string) to False (boolean)

def sum_even(start, end):
    sum = 0
    for i in range(start, end):  
        if is_even(i):  # Function correctly returns boolean
            sum += i
    return sum

try:
    start = int(input("Enter the start number: "))  
    end = int(input("Enter the end number: "))  # Convert input to integer

    if start > end:
        print("Error: Start number should be less than or equal to the end number.")
    else:
        print("The sum of all even numbers is", sum_even(start, end))

except ValueError:
    print("Invalid input! Please enter integer values.")
