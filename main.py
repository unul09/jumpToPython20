# 2
try:
    a = {'A': 90, 'B': 80}
    print(a['C'])

except KeyError:
    a['C'] = 70
    print(a['C'])
