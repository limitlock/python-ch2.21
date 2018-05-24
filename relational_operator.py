
# 객체의 대소
print(1 > 3)
print(2 < 4)

print(5 >= 4)
print(6 == 9)
print(6 != 9)


# 복합 관계식 지원

a = 6
print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 다른 타입의 객체 비교
print("abcd" > "abc")
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] < [1, 2, 0])

# 동질성 비교
a = 10
b = 20
c =a
print(a == b)
print(a is b)
print(a is c)
print(a == c)
