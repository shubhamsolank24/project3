def sqrt(target):
 
    if target < 0:
        return None
    if target <= 1:
        return target

    lowest, highest = 2, target // 2

    while lowest <= highest:
        candidate = ((highest - lowest) // 2) + lowest
        sq_candidate = candidate * candidate

        if sq_candidate == target:
            return candidate

        if sq_candidate > target:
            highest = candidate - 1
        else:
           
            sq_candidate_plus = (candidate + 1) * (candidate + 1)
            if sq_candidate_plus > target:
                return candidate
            lowest = candidate + 1

 
    return None


if __name__ == '__main__':
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    print("Pass" if (31 == sqrt(999)) else "Fail")
    print("Pass" if (92 == sqrt(8572)) else "Fail")
    print("Pass" if (436 == sqrt(190292)) else "Fail")
