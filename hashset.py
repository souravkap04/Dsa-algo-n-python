# LeetCode 217 — Contains Duplicate 

def isDuplicate(nums):
    seen = set()
    for x in seen:
        if x in seen:
            return True
        seen.add(x)
    return False

nums = [1,2,3,1]
print(isDuplicate(nums))

# =====================================================

# LeetCode 349 — Intersection of Two Arrays

def intersection(nums1,nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        answer = []
        for x in set2:
            if x in set1:
                answer.append(x)
        return answer     

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1,nums2))    

# ===========================================================================================
# LeetCode 268 — Missing Number


def missingNumber(nums):
        s = set(nums)

        for i in range(len(nums) + 1):
            if i not in s:
                return i
            


print(missingNumber(nums=[3,0,1,2]))

# ==========================================================================================================

# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.

def singleNumber(nums):
     
    seen = set()
    for x in nums:
          
        if x in seen:
            seen.remove(x)

        else :
            seen.add(x)  

    return seen.pop()

nums = [4,1,2,1,2]
print(singleNumber(nums))

# ========================================================================================

# Leetcode 202 Happy Number 

def isHappy(n):

        seen = set()

        while n != 1:

            result = 0  
            if n in seen:
                return False
            seen.add(n)
            while n > 0:
                rem = n % 10
                result += rem * rem
                n //= 10
            n = result
        return True
        

n = 19
print(isHappy(n))           

# ================================================================
#  LeetCode 3 — Longest Substring Without Repeating Characters 
#  LeetCode 128 — Longest Consecutive Sequence 
#  LeetCode 49 — Group Anagrams (introduces HashMap + hashing)
