# 20
import re

p = re.compile(".*[@].*[.](?=com$|net$).*$")
print(p.match("morning20404@gmail.com"))
print(p.match("morning20404@ewhain.net"))
print(p.match("morning20404@ewha.ac.kr"))
# 정규표현식줫나어렵네~~~~~ 씌벌