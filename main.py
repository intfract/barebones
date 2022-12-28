def max(a, b):
    return a - ((a - b - abs(a - b)) / 2)

print(max(0, 1)) # 1
print(max(1, -1)) # 1
print(max(-1, -2)) # -1

def min(a, b): # (1 / 3) cases
    return a + ((a - b + abs(a - b)) / 2)

print(min(0, 1)) # 0
print(min(1, -1)) # -1
print(min(-1, -2)) # -2