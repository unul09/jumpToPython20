# 14
a = str(input("압축할 문자열 입력 : ")) + ' '
print(a)
b = ''
count = 1
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        count += 1
    else:
        b += a[i] + str(count)
        count = 1
print(b)