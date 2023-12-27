import re
from fileinput import input

word2digit = {
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

dig_re = re.compile(f'(?=(\d|{"|".join(word2digit.keys())}))')
r = re.compile(rf'^.*?(\d)')
ans = []
for i,line in enumerate(input()):
    line = line.strip()

    # print(line)

    digits = dig_re.findall(line)

    # print(line, end='\n\n')

    fst = digits[0]  if digits[0].isdigit()  else str(word2digit[digits[0]])
    lst = digits[-1] if digits[-1].isdigit() else str(word2digit[digits[-1]])

    print(i, fst + lst)

    ans.append(int(fst + lst))

print(sum(ans))
