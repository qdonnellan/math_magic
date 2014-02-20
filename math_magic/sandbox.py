import re
import random

# just a sandbox for trying things out
# this is mostly old stuff that I haven't transferred into the project yet

prb = '(1,4]**2 + [1,4]**2'

pattern = re.compile("[\(\[]\d+,\d+[\)\]]")
results = re.findall(pattern, prb)

for result in results:
    a = int(re.search('(\d+),', result).group(1))
    b = int(re.search(',(\d+)', result).group(1))
    if '(' in result: 
        a += 1
    if ')' in result: 
        b += 1
    r = random.randint(a,b)
    prb = re.sub(pattern, str(r), prb, count=1)

print prb

