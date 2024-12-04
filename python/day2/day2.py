def file_to_lst(f) -> list[list[int]]:
    with open(f) as f_txt:
        lst = [[int(x) for x in line.split()] for line in f_txt]
    return lst

def is_monotonic(lst: list[int]) -> bool:
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

def difference(lst: list[int]) -> bool:
    return all(1 <= abs(lst[i] - lst[i - 1]) <= 3 for i in range(1, len(lst)))

def remove_element_combs(lst: list[int]) -> list[list[int]]:
    return [lst[:i] + lst[i + 1:] for i in range(len(lst))]

def safe_lst(lst: list[list[int]]) -> tuple[int, int]:
    safe, moresafe = 0, 0
    for i in lst:
        if is_monotonic(i) and difference(i):
            safe += 1
        for j in remove_element_combs(i):
            if is_monotonic(j) and difference(j):
                moresafe += 1
                break  
    return safe, moresafe

lst = file_to_lst("day2.txt")
print(safe_lst(lst))
