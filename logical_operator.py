
# 논리식의 계산 순서
print([] or 'logical')
print('logical' or 'operator')
print('' or 'opeprator')

print(None and 1)
print(None or [])

None or print([])


# 논리 연산자

a = 20
b = 30
print(not a < b)
print(a < b)

print(a < b and a != b)
print(a == b or a != b)

# True -> 1 False -> 0
print(True + 1)
print((a > b) + 1)

# bool 캐스팅
print(bool(10), bool(0))
print(bool(3.14), bool(0.))
print(bool("abc"), bool(""))
print(bool([1, 2, 3,]), bool([]))
print(bool({"a": 2}), bool({}))
print(bool(None))











