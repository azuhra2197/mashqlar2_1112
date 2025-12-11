# 6
def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

result = tuple(i for i in range(1, 31) if is_prime(i))
print(result)

# 7
lst = [-4, 7, 0, 12, -1, 3]
result = tuple(i for i in lst if i > 0)
print(result)

# 8
result = tuple((i, i*i) for i in range(1, 16))
print(result)

# 9
text = "Python tuple comprehension misollari"
words = text.split()
result = tuple(w[-1] for w in words)
print(result)

# 10
lst = list(range(1, 21))
result = tuple(lst[i]**2 for i in range(len(lst)) if i % 2 == 1)
print(result)

