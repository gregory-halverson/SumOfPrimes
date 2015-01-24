__author__ = 'gregory'

def is_prime(n):
    for i in range(2, n):
        if not n % i:
            return False

    return True

i = 2
count = 0
sum = 0

while (count < 1000):
    if is_prime(i):
        sum += i
        count += 1

    i += 1

print(sum)