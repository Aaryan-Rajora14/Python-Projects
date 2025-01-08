def mean():
    b = sum(a)
    c = b / n
    print(f'The Sum is {b} and Mean is {c}')

def median():
    if n % 2 == 0:
        b = (a[n // 2 - 1] + a[n // 2]) / 2
    else:
        b = a[n // 2]
    print(f'The Median is {b}')

def mode():
    f = {}
    for num in a:
        if num in f:
            f[num] += 1
        else:
            f[num] = 1
    b = max(f, key=f.get)
    print(f"The Mode is {b}")

while True:
    a = list(map(int, input("Enter list of Numbers: ").split(",")))
    a.sort()
    n = len(a)
    ch = int(input('Select Your Choice 1 for MEAN 2 for MEDIAN 3 for MODE: '))
    if ch == 1:
        mean()
    elif ch == 2:
        median()
    elif ch == 3:
        mode()
    else:
        print("Thanks For Using Program")
        break
