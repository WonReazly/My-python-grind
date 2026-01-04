num = int(input())
numbers = [int(input()) for _ in range(num)]
numberskvad = []
for c in numbers:
    lol = 0
    lol += c**2+2*c+1
    numberskvad.append(lol)
print(*numbers, sep = '\n')
print()
print(*numberskvad, sep = '\n')


