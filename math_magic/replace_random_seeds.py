import re
import random

def replace_random_seeds(user_input):
    '''
    replace instances of [a..b], (a..b), (a..b], and [a..b) with a random number N such that
    a < N < b (with left or right inclusiveness according to left-right parentheses/bracket behavior)
    '''
    pattern = re.compile("[\(\[]\d+..\d+[\)\]]")
    results = re.findall(pattern, user_input)

    for result in results:
        a = int(re.search('(\d+)[.][.]', result).group(1))
        b = int(re.search('[.][.](\d+)', result).group(1))
        if '(' in result: 
            a += 1
        if ')' in result: 
            b -= 1
        r = random.randint(a,b)
        user_input = re.sub(pattern, str(r), user_input, count=1)

    return user_input


