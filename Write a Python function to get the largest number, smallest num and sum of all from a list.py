l = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    l.append(numbers)
print("Maximum element in the list is :", max(l), "\nMinimum element in the list is :", min(l))
