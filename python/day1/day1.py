def file_to_lst(f) -> tuple[list[int], list[int]]:
    with open(f) as f_txt:
        lst = [[int(x) for x in line.split()] for line in f_txt]
    lst1 = [row[0] for row in lst]
    lst2 = [row[1] for row in lst]
    return lst1, lst2
 
def day1(lst1, lst2) -> tuple[int, int]:
    p1 = 0 
    p2 = 0
    for i in range(len(lst1)):
        if lst1[i] > lst2[i]:
            p1 += (lst1[i] - lst2[i])
        else:
            p1 += (lst2[i] - lst1[i])
        p2 += (lst1[i] * lst2.count(lst1[i])) # lol thx python
    return p1, p2

f = file_to_lst("day1.txt")
lst1, lst2 = sorted(f[0]), sorted(f[1]) # python has a sorted function, rip my quicksort
print(day1(lst1, lst2))
