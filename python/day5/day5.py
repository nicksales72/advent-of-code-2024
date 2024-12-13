def file_to_lsts(f) -> tuple[list[str], list[str]]:
    lst1 = []
    lst2 = []
    with open (f, "r") as file:
        for line in file:
            stripped_line = line.strip()
            if "|" in stripped_line:
                lst1.extend(stripped_line.split("|"))
            else:
                lst2.append(stripped_line.split(","))
    seen = {}
    for index, value in enumerate(lst1):
        seen[value] = index 
    lst1 = sorted(seen.keys(), key=lambda x: seen[x])
    return lst1, lst2

def valid_lsts(lst, prior_lst):
    valid_lst = []
    for i in range(len(lst)):
        for j in range(1, len(lst[i])):
            if lst[i][j-1] in prior_lst:

    return valid_lst

idk = file_to_lsts("day5.txt")
