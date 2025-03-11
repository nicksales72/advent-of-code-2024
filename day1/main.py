def process_file(file:str) -> tuple[list[int], list[int]]:
    with open(file, "r") as f:
        pairs = [x.strip().split() for x in f]
        col1 = [int(pair[0]) for pair in pairs]
        col2 = [int(pair[1]) for pair in pairs]
    col1.sort()
    col2.sort()
    return col1, col2

def solve_thing(lst1:list[int], lst2:list[int]) -> tuple[int, int]:
    part1 = 0
    part2 = 0
    for i in range(len(lst1)):
        part1 += abs(lst1[i] - lst2[i]) # distances
        part2 += lst1[i] * lst2.count(lst1[i]) # occurrences 
    return part1, part2

if __name__ == "__main__":
    lst1, lst2 = process_file("input.txt")
    answer = solve_thing(lst1, lst2)
    print(answer)