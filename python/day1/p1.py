def file_to_lst(f):
    with open(f) as f_txt:
        lst = [[int(x) for x in line.split()] for line in f_txt]
    lst1 = [row[0] for row in lst]
    lst2 = [row[1] for row in lst]
    return lst1, lst2

def quicksort_list(lst):
    if len(lst) <= 1:
        return lst
    p = lst[len(lst) // 2]
    l = [x for x in lst if x < p]
    m = [x for x in lst if x == p]
    r = [x for x in lst if x > p]
    return quicksort_list(l) + m + quicksort_list(r)
    

f = file_to_lst("p1.txt")
lst1 = quicksort_list(f[0])
lst2 = quicksort_list(f[1])
sum = 0 
for i in range(len(lst1)):
    if lst1[i] > lst2[i]:
        sum += (lst1[i] - lst2[i])
    else:
        sum += (lst2[i] - lst1[i])
print(sum)
