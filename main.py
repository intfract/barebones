def max(a, b):
    x = a - b
    return a - ((x - abs(x)) / 2)

print(max(0, 1)) # 1
print(max(1, -1)) # 1
print(max(-1, -2)) # -1

def min(a, b):
    x = a - b
    return a - ((x + abs(x)) / 2)

print(min(0, 1)) # 0
print(min(1, -1)) # -1
print(min(-1, -2)) # -2