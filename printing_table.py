import itertools
n  = int(input('Enter the number : '))
counter = itertools.count(start = n, step = n)
print('________Your_Lucky_Table_Is_________')
for i in range(10):
    print(next(counter))
