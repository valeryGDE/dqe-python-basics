import random

# Create a list of 100 random numbers in the range of 0 to 1000
random_list = [random.randint(0, 1000) for _ in range(100)]

# Print the random list
print("Random list:", random_list)


# Define a function called "bubble_sort" that takes a list of numbers as input
def bubble_sort(nums):
    # For every element in the list (except the last element)
    for i in range(len(nums) - 1):
        # For every element in the list up to the last sorted element
        for j in range(len(nums) - i - 1):
            # If the current number is greater than the next number,
            if nums[j] > nums[j + 1]:
                # Swap the current number with the next number
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    # Return the sorted list
    return nums


# Print the result of sorting the random list
print("Sorted list:", bubble_sort(random_list))


# Define a function named "average_even_odd" that takes a list of numbers as input
def average_even_odd(nums):
    # Initialise variables to hold the cumulative sum and count of even numbers
    sum_even, count_even = 0, 0
    # Initialise variables to hold the cumulative sum and count of odd numbers
    sum_odd, count_odd = 0, 0
    # Loop over each number in the input list
    for num in nums:
        # If the number is even (i.e., remainder of num / 2 is 0)
        if num % 2 == 0:
            # Add it to the sum of even numbers
            sum_even += num
            # Increment the count of even numbers
            count_even += 1
        # If the number is not even (it's odd)
        else:
            # Add it to the sum of odd numbers
            sum_odd += num
            # Increment the count of odd numbers
            count_odd += 1

    # Calculate the average of even numbers by dividing the sum by the count
    avg_even = sum_even / count_even
    # Calculate the average of odd numbers by dividing the sum by the count
    avg_odd = sum_odd / count_odd if count_odd > 0 else 0

    # Return the average of even and odd numbers
    return avg_even, avg_odd


# Call the function with the random list of numbers, and store the returned even and odd averages
average_even, average_odd = average_even_odd(random_list)

# Print the average of even numbers
print("Average of even numbers:", average_even)
# Print the average of odd numbers
print("Average of odd numbers:", average_odd)
