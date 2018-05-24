
a = 1.2

print(type(a))
print(isinstance(a, float))

# Integer 값인가? (값으로 판별) = > true
b = 2.0
print(b.is_integer())

# 다른 언어처럼 소수점이나 e, E로 지수 표현이 가능하다.
b = 3e3
c = -0.2e-4
print(a, b, c)
print(type(b))

