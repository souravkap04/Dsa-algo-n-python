def two_sum(nums,target):
    left = 0
    right = len(nums) - 1
    while left < right :
        current = nums[left] + nums[right]
        if current == target:
            return nums[left] , nums[right]
        elif current < target :
            left += 1
        else :
            right -= 1    

nums = [1,2,3,4,5,6,7,8]
target = 10
print(two_sum(nums,target)) 
# ===========================================================================================     

def moveZeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow],nums[fast] = nums[fast],nums[slow]
            slow += 1
    
    return nums     

nums = [0,1,0,3,12]
print(moveZeros(nums))

# ===========================================================================================

def isPalindromy(s):
    left = 0
    right = len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    return True

s = "madam"
print(isPalindromy(s))    

# ================================================================================================

def removeDuplicate(nums):
    slow = 0
    for fast in range(1,len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return nums[:slow+1]    

nums = [1,1,2,2,3]
print(removeDuplicate(nums))   

# ====================================================================================================

def reverseString(s):
    left = 0
    right = len(s) -1
    while left < right:
        chars[left],chars[right] = chars[right],chars[left]
        left += 1
        right -= 1
    return chars

chars = ['h', 'e', 'l', 'l', 'o']
print(reverseString(chars))    