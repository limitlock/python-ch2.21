for a in range(3,100,3):
    s = a//10
    if s % 3 == 0 and a % 10 != 0 and a > 10:
        print('%d 짝짝' % a)
    else:
        print('%d 짝' % a)
