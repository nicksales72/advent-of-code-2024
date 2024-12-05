import re

def file_to_text(f) -> str:
    with open(f) as f_txt: 
        text = f_txt.read()
    return text

def find_muls(t) -> list[str]:
    return re.findall(r"mul\(\d+,\d+\)", t)

def multiply_pairs(t) -> int:
    sum = 0 
    for i in t:
        match = re.search(r"\((\d+),\s*(\d+)\)", i)
        if match:
            x, y = map(int, match.groups())
            sum += x * y
    return sum

txt = file_to_text("day3.txt")
print(multiply_pairs(find_muls(txt)))
