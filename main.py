# 15
data_bunch = input().split()
for data in data_bunch:
    nums = []
    for s in data:
        nums.append(int(s))
    nums.sort()
    right_data = [0,1,2,3,4,5,6,7,8,9]
    print(nums == right_data, end=' ')