num = int(input('금액:'))

arr = []
a = 50000
b = 40000
count = 0
while True:
    arr.append(num/a)
    num = num % a
    if count % 2 != 0:
        a = int(a/2)
    else:
        a = a - b
        b = b / 10
    count += 1

    if a < 1:
        break

for ret in arr:
    print(int(ret))
