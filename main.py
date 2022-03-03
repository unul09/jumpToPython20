# 19
import re
data = """
park 010-9999-9900
kim 010-2222-4433
lee 010-2351-0033
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", data)
print(result)

