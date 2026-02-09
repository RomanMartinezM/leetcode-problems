def calculate_maximum_amoun_of_water(height):
    max = 0
    left = 0
    right = len(height) - 1

    while left < right:
        if height[left] < height[right]:
            lowest = height[left]
            x = right - left
            amount = x * lowest
            if amount > max:
                max = amount
            left += 1
        else:
            lowest = height[right]
            x = right - left
            amount = x * lowest
            if amount > max:
                max = amount
            right -= 1
            
    return max


def main():
    test_cases = [
        [1,8,6,2,5,4,8,3,7],   # basic example
        [1,1],                 # minimum size
        [1,2,3,4,5],           # increasing heights
        [5,4,3,2,1],           # decreasing heights
        [5,5,5,5,5],           # all equal
        [10,1,1,1,10],         # tall ends
        [1,2,100,2,1],         # tall middle peak
        [2,3,4,5,18,17,6],     # zig-zag
        [1000,1,1000],         # large values
        [4,3,2,1,4],           # symmetric
    ]

    for i in range(len(test_cases)):
        print("-"*100)
        print(i+1, ".\t", test_cases[i], " total elements: ", len(test_cases[i]), sep="", end="")
        print("result: ", calculate_maximum_amoun_of_water(test_cases[i]), sep="", end="")
        print("-"*100)

if "__name__" == main:
    main()