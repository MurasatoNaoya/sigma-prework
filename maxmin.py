def find_max_min(nums):
    # Setting placeholder values for min and max. 
    max, min = float('-inf'), float('inf')

    for n in nums:
        # Check for a new maximum.
        if n > max:
            max =  n
        # Check for a new minimum.
        if n < min:
            min = n

    # Return tuple of max and min 
    return (max, min)

# Test cases. 
# nums = [1, 2, 3, 4, 5]
# print(find_max_min(nums))

nums = [1, 2, 3, 4, 5]

if __name__ == '__main__':
    print(find_max_min(nums))