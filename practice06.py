

input = list(map(int, input('리스트를 입력하세요 : ').split()))
count = 0
sum = 0

for i in input:
    if i % 3 == 0:
        count += 1
        sum += i
print('주어진 리스트에서 3의 배수의 개수=> '+str(count))
print('주어진 리스트에서 3의 배수의 합=> '+str(sum))


