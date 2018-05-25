num = list(map(int,input('5개의 숫자를 입력하세요.').split()))
avg = 0
for a in range(len(num)):
    avg += num[a]
print(avg/len(num))
