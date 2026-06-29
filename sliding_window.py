def max_sum_subarray(nums , k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k,len(nums)):
        window_sum = window_sum - nums[i-k] +nums[i]
        max_sum = max(max_sum,window_sum)
        
    return max_sum
    
    
nums = [2,1,5,1,3,2]
k = 3 
print(max_sum_subarray(nums,k))

# ======================================================================================

def max_sum_subarray(nums, k):

    left = 0
    window = 0
    answer = float("-inf")

    for right in range(len(nums)):

        # Add current element
        window += nums[right]

        # Window size becomes k
        if right - left + 1 == k:

            # Update answer
            answer = max(answer, window)

            # Remove left element
            window -= nums[left]

            # Move left pointer
            left += 1

    return answer


nums = [2,1,5,1,3,2]
k = 3 
print(max_sum_subarray(nums,k))

# ===============================================================================
# Q) Minimum Size Subarray Sum / Find the minimum length of a subarray whose sum is at least target.
# variable length sliding window

def min_subarray_len(target, nums):

    left = 0
    window = 0
    answer = float("inf")

    for right in range(len(nums)):

        # Expand
        window += nums[right]

        # Shrink
        while window >= target:

            answer = min(answer, right - left + 1)

            window -= nums[left]
            left += 1

    return 0 if answer == float("inf") else answer
    
    
k = 7
nums = [2,3,1,2,4,3]
print(min_subarray_len(k,nums))    

# =================================================================================================
# Longest Substring Without Repeating Characters
# variable length sliding window

def length_of_longest_substring(s):
    left = 0
    window = {}
    answer = 0
    for right in range(len(s)):
        window[s[right]] = window.get(s[right],0) +1
        while window[s[right]] > 1:
            window[s[right]] -= 1
            left += 1
            answer = max(answer,right-left+1)
            
    return answer    
    
s = 'abcabbcbca' 
# s = "abcabcbb"
print(length_of_longest_substring(s))
