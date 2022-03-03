# 14
data = input()
_c = data[0]    #반복중인 문자
result = data[0]
cnt = 0
for c in data:
    if c != _c:
        result += str(cnt)
        result += c
        cnt = 1
        _c = c
    else:
        cnt += 1

result += str(cnt)

print(result)