def file_to_lst(f) -> tuple[list[int], list[int]]:
    with open(f) as f_txt:
        lst = [[x for x in line] for line in f_txt]
    return lst

def is_within_bounds(lst, i, j):
    return 0 <= i < len(lst) and 0 <= j < len(lst[i])

def xmas_check(lst, i, j):
    xmas = 0
    directions = [
        (0, 1), (0, -1),
        (1, 0), (-1, 0),  
        (1, 1), (1, -1),
        (-1, 1), (-1, -1) 
    ] 
    for di, dj in directions:
        if all(
            is_within_bounds(lst, i + k * di, j + k * dj) 
            and lst[i + k * di][j + k * dj] == "XMAS"[k]
            for k in range(4)
        ):
            xmas += 1
    return xmas

def mas_check(lst, i, j):
    mas = 0
    mas_patterns = [
        [("S", "S"), ("M", "M")],
        [("M", "M"), ("S", "S")],
        [("M", "S"), ("M", "S")],
        [("S", "M"), ("S", "M")],
    ]
    if lst[i][j] == "A":
        for top, bottom in mas_patterns:
            if (
                is_within_bounds(lst, i - 1, j - 1)
                and is_within_bounds(lst, i - 1, j + 1)
                and is_within_bounds(lst, i + 1, j - 1)
                and is_within_bounds(lst, i + 1, j + 1)
                and lst[i - 1][j - 1] == top[0]
                and lst[i - 1][j + 1] == top[1]
                and lst[i + 1][j - 1] == bottom[0]
                and lst[i + 1][j + 1] == bottom[1]
            ):
                mas += 1
                break
    return mas

def matches(lst):
    xmas = 0
    mas = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            xmas += xmas_check(lst, i, j)
            mas += mas_check(lst, i, j)
    return xmas, mas

lst = file_to_lst("day4.txt")
print(matches(lst))
