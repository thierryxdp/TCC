def filtra_pares(nums):
    nums_pares = []
    if nums[0]%2 == 0:
        nums_pares[0] = nums[0]
    if nums[1]%2 == 0:
        nums_pares[1] = nums[1]
    if nums[2]%2 == 0:
        nums_pares[2] = nums[2]
    if nums[3]%2 == 0:
        nums_pares[3] = nums[3]
    
    return (nums_pares[0], nums_pares[1], nums_pares[2], nums_pares[3])