# Two sum

def two_sum(nums,target):
    mapping = {}
    for i , value in enumerate(nums):
        current = target - value
        if current in mapping:
            return [mapping[current],i]
        mapping[value] = i

nums = [2,7,11,15] 
target = 9
print(two_sum(nums,target))

# ====================================================================
# Contains Duplicate (217)
def isDuplicate(nums):
    mapping = {}
    for i , value in enumerate(nums):
        if value in mapping:
            return True
        mapping[value] = i
    return False

nums = [1,2,3,1]
print(isDuplicate(nums))

# ================================================================
# Longest Substring Without Repeating Characters(3)
# two pointer + hashmap index mapping

def lengthOfLongestSubsstring(s):
    left = 0
    max_len = 0
    last_seen = {}
    for right in range(len(s)):
        if s[right] in last_seen and last_seen[s[right]] >= left:
            left = last_seen[s[right]] + 1
        last_seen[s[right]] = right
        max_len = max(max_len,right - left + 1)

    return max_len

s = "pwwkew"
print(lengthOfLongestSubsstring(s))


