# 9
f = open('sample.txt')
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
avg = total / len(lines)

f = open('result.txt', 'w')
f.write(str(avg))
f.close()