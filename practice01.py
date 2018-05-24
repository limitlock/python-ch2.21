# 1번

a = input('수를 입력하세요:')

if(a.isdigit() != True):
    print("정수가 아닙니다")
else:
    if(int(a) % 3 == 0):
        print('3의 배수입니다.')
    else:
        print('3의 배수가 아닙니다.')


