def file_to_lst(f) -> tuple[list[int], list[int]]:
    with open(f) as f_txt:
        lst = [[int(x) for x in line.split()] for line in f_txt]
    lst1 = [row[0] for row in lst]
    lst2 = [row[1] for row in lst]
    return lst1, lst2

def quicksort_lst(lst) -> list[int]:
    if len(lst) <= 1:
        return lst
    p = lst[len(lst) // 2]
    l = [x for x in lst if x < p]
    m = [x for x in lst if x == p]
    r = [x for x in lst if x > p]
    return quicksort_lst(l) + m + quicksort_lst(r)
    
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
lst1 = quicksort_lst(f[0])
lst2 = quicksort_lst(f[1])
print(day1(lst1, lst2))
