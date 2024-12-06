import re

def file_to_text(f) -> str:
    with open(f) as f_txt: 
        text = f_txt.read()
    return text

def find_muls(t) -> list[str]:
    return re.findall(r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))", t)

def remove_muls(lst) -> list[str]:
    new_lst = []
    flag = True
    for i in lst:
        if i == "don't()":
            flag = False
            continue
        if i == "do()":
            flag = True
            continue
        if flag:
            new_lst.append(i)
    return new_lst

def multiply_pairs(t) -> int:
    sum = 0 
    for i in t:
        match = re.search(r"\((\d+),\s*(\d+)\)", i)
        if match:
            x, y = map(int, match.groups())
            sum += x * y
    return sum

txt = file_to_text("day3.txt")
muls = find_muls(txt)
muls_pt2 = remove_muls(muls)
print(multiply_pairs(muls), multiply_pairs(muls_pt2))
