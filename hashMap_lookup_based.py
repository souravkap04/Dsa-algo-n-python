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

# ====================================================================================================================================
# Q Word Pattern (LeetCode 290) 

def word_pattern(pattern , s):
    word = s.split()
    p_to_w = {}
    w_to_p = {}
    if len(pattern) != len(word):
        return False
    for p , w in zip(pattern,word):
        if p in p_to_w :
            if p_to_w[p] != w:
                return False
        else :
            p_to_w[p] = w

        if w in w_to_p:
            if w_to_p[w] != p:
                return False
        else :
            w_to_p[w] = p

    return True

pattern = "abba"
s= "dog cat cat dog"
print(word_pattern(pattern , s))


# ===========================================================================================================
# Q 


def isIsomorphic(self, s: str, t: str) -> bool:
    lookup1 = {}
    lookup2 = {}
    if len(s) != len(t):
        return False
    for ch1 , ch2 in zip(s,t):
        if ch1 in lookup1:
            if lookup1[ch1] != ch2:
                return False
        else :
            lookup1[ch1] = ch2


        if ch2 in lookup2:
            if lookup2[ch2] != ch1:
                    return False

        else :
            lookup2[ch2] = ch1
    
    return True

s="title"
t = "paper"
print(isIsomorphic(s,t))             

