# LeetCode-303 Range Sum Query - Immutable
def range_sum_query(nums,left,right):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix[right+1] - prefix[left]

nums = [2,4,1,6,3]
left = 1
right = 4
print(range_sum_query(nums,left,right))

# ===================================================================

# LeetCode - 1480 Running Sum of 1d Array

def running_sum(nums):
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix[1:]



nums = [1,2,3,4]
print(running_sum(nums))

# ======================================================================

# 724. Find Pivot Index 

def pivot_index(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    return -1



nums = [1,7,3,6,5,6]
print(pivot_index(nums))
# =====================================================================

# 560. Subarray Sum Equals K 
# prefix sum + hash map

from collections import defaultdict
def sub_array_sum(nums,k):
    count = 0
    current_sum = 0
    prefix_freq = defaultdict(int)
    prefix_freq[0] = 1
    for num in nums:
        current_sum += num
        need = current_sum -k
        if need in prefix_freq:
            count += prefix_freq[need]
        prefix_freq[current_sum] += 1
    return count

nums = [1,2,1,2,1]
k=3
print(sub_array_sum(nums,k))

# ========================================================
# 525. Contiguous Array
# hashmap + prefix sum 

def find_max_length(nums):
    count = 0
    max_len = 0
    hash = defaultdict(int)
    hash[0] = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        if count in hash:
            max_len = max(max_len,i-hash[count])
        else :
            hash[count] = i
    return max_len

nums = [0,1,1,1,1,1,0,0,0]
print(find_max_length(nums))




