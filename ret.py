__author__ = 'X'
import re
import math
#test=r'\d{2,3}-?\d{6,8}'
#re.findall(test,'010-3317897')
r = r'(w{3}\..+\.(?:com|org))'
print(re.findall(r,'www.baidu.com'))

import os
print(os.name)
