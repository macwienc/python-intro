import math

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

combined = list(zip(list1, list2))

print("Combined lists:", combined)

try:
    result = math.sqrt(-1)
    print("Result of sqrt(-1):", result)
except ValueError as e:
    print("Caught ValueError:", e)
except Exception as e:
    print("Caught another exception:", type(e), e)
