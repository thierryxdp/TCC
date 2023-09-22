def filtra_pares(nums):
    nums_pares = []
    if nums[0]%2 == 0:
        nums_pares.append(nums[0])
    if nums[1]%2 == 0:
        nums_pares.append(nums[1])
    if nums[2]%2 == 0:
        nums_pares.append(nums[2])
    if nums[3]%2 == 0:
        nums_pares.append(nums[3])
    
    return (nums_pares)