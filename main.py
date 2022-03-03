# 13
# 11, 12는 코드작성 없는 문제이므로 추가하지 않았음

def DashInsert(numbers):
    result = []
    for i in range(len(numbers)):
        result.append(str(numbers[i]))
        if i == len(numbers) - 1: break
        if numbers[i] % 2 == 0:
            if numbers[i + 1] % 2 == 0: result.append('*')
        else:
            if numbers[i + 1] % 2 == 1: result.append('-')
    result = ''.join(result)
    return result


numbers = list(map(int, input()))
print(DashInsert(numbers))