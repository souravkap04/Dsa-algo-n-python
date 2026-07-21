# Group Anagrams (LeetCode 49) 

from collections import defaultdict
def group_anagram(strs):
    groups = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram(strs))

# =====================================================================================

# Categorize Products
def categorize_product(products):
    groups = defaultdict(list)
    for product , category in products:
        groups[category].append(product)
    return dict(groups)
    
    
products = [
    ("Laptop", "Electronics"),
    ("TV", "Electronics"),
    ("Apple", "Food"),
    ("Banana", "Food"),
    ("Soap", "Personal Care")
]
print(categorize_product(products))
# ============================================================================

# Categorize by age

def categorize_by_age(people):
    groups = defaultdict(list)
    for name,age in people:
        key = age
        groups[key].append(name)
    return dict(groups)


people = [
("Alice",25),
("Bob",30),
("Charlie",25),
("David",30),
("Eva",35)
]
print(categorize_by_age(people))

# ============================================================