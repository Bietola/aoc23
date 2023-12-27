import re
from fileinput import input

digits = {
    # 'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

dig_re = re.compile('|'.join(digits.keys()))
r = re.compile(rf'^.*?(\d)')
ans = []
for line in input():
    line = line.strip()

    print(line)

    line = dig_re.sub(lambda m: str(digits[m.group(0)]), line)

    print(line, end='\n\n')

    fst = m.group(1) if (m := r.match(line)) else None
    lst = m.group(1) if (m := r.match(line[::-1])) else None

    ans.append(int(fst + lst))

print(sum(ans))
