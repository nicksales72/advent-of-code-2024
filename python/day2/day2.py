def file_to_lst(f) -> list[list[int]]:
    with open(f) as f_txt:
        lst = [[int(x) for x in line.split()] for line in f_txt]
    return lst

def safe_lst(lst) -> int:
    safe = 0 
    safe1 = 0
    for i in range(len(lst)):
        sorted_lst = sorted(lst[i])
        if lst[i] == sorted_lst or lst[i] == sorted_lst[::-1]:
            safe += 1
            for j in range(1, len(lst[i])):
                if abs(lst[i][j] - lst[i][j - 1]) < 1 or abs(lst[i][j] - lst[i][j - 1]) > 3:
                    safe -= 1 
    return safe

lst = file_to_lst("day2.txt")
print(safe_lst(lst))
