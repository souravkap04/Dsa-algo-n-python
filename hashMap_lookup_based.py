#Q Two Sum 

def two_sum(nums,target):
    lookup = {}
    for i , num in enumerate(nums):
        need = target - num
        if need in lookup:
            return lookup[need] ,i
        lookup[num] = i



nums = [2,7,11,5]
target = 12
print(two_sum(nums,target))    

# ===============================================================================

# Q Contains Duplicate 

def find_duplicate(nums):
    lookup = {}
    for i ,num in enumerate(nums):
        
        if num in lookup:
            return True
        lookup[num] = i
    return False    

nums = [1,2,3,3,5]
print(find_duplicate(nums))

# ===================================================================================
# Q Find Happy Number
def is_happy(n):
    lookup = {}

    while n != 1:

        # If we've seen this number before, we're in a cycle
        if n in lookup:
            return False

        # Remember this number
        lookup[n] = True

        # Calculate the sum of the squares of the digits
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return True


print(is_happy(19))   # True
print(is_happy(2))    # False       

