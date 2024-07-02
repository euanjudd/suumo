jumps=[nums[0]]
while True:
    if jumps[0] <= 0:
        return False
    elif jumps[-1] <= 0:
        del jumps[-1]
        jumps[-1] -= 1
    elif sum(jumps) < len(nums) - 1:
        jumps.append(sum(jumps))
    elif sum(jumps) >= len(nums) - 1:
        return True
return False