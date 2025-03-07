def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False  # Changed "false" (string) to False (boolean)

def sum_even(start, end):
    ttl = 0  #Changed 'sum' to 'ttl' to avoid conflict with built-in function
    for i in range(start, end + 1):  # Include 'end' in the range
        if is_even(i):
            ttl += i
    return ttl

try:
    start = int(input("Enter the start number: "))  
    end = int(input("Enter the end number: "))  # Convert input to integer

    if start > end:
        print("Error: Start number should be less than or equal to the end number.")
    else:
        print("The sum of all even numbers is", sum_even(start, end))

except ValueError:
    print("Invalid input! Please enter integer values.")
