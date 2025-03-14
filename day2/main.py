def process_file(file:str) -> list[list[int]]:
    with open(file, "r") as f:
        lsts = [[int(num) for num in x.strip().split()] for x in f]
    return lsts

def is_monotonic(lst:list[int]) -> bool:
    return (lst == sorted(lst)[::-1] or lst == sorted(lst))

def correct_difference(lst:list[int]) -> bool:
    for i in range(len(lst) - 1):
        if abs(lst[i] - lst[i + 1]) > 3 or abs(lst[i] - lst[i + 1]) < 1:
            return False
    return True

def get_subsets(lst:list[int]) -> list[list[int]]:
    length = len(lst) - 1
    res = [[]]
    for i in lst:
        res += [sub + [i] for sub in res] 
    return [sub for sub in res if len(sub) == length] # lets be even slower!

def solve(lsts:list[list[int]]) -> tuple[int, int]:
    part1 = 0
    part2 = 0
    for lst in lsts:
        if is_monotonic(lst) and correct_difference(lst):
            part1 += 1
            part2 += 1
        else:
            subsets = get_subsets(lst)
            for subset in subsets:
                if is_monotonic(subset) and correct_difference(subset):
                    part2 += 1
                    break
    return part1, part2

if __name__ == "__main__":
    lsts = process_file("input.txt")
    answer = solve(lsts)
    print(answer)