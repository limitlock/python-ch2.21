num = int(input('숫자를 입력하세요: '))

ret = 0
if num%2 != 0:
    for i in range(num+1):
        if i%2 != 0:
            ret += i
else:
    for i in range(num+1):
        if i%2 == 0:
            ret += i

print('결과 값 : '+str(ret))
