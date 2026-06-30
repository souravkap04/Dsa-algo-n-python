# Frequency Based Hash Map Implementation
# Q. Count the frequency of each integer in an array.
def count_freq(nums):
    freq = {}
    for i in range(len(nums)):
        freq[nums[i]] = freq.get(nums[i],0) + 1
    return freq    

nums = [4,2,3,5,4,2,5,1]  
print(count_freq(nums))

# =======================================================================================
# Q Find all duplicate elements in an array.

def find_duplicate(nums):
    freq = {}
    for i in range(len(nums)):
        freq[nums[i]] = freq.get(nums[i],0) + 1

    for key in freq:
        if freq[key] > 1:
            print(key)    

nums = [4,2,3,5,4,2,5,1]  
find_duplicate(nums)

# ====================================================================================
#  Find the first non-repeating character in a string.

def non_repeating_char(s):
    freq = {}
    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i],0) + 1
    
    for ch in s:  
        if freq[ch] == 1:
            print(ch)
            break
        
s ="ssdderftty" 
non_repeating_char(s)   