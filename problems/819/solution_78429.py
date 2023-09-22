def filtraMultiplos(nums,n):
    """ """
    i=0
    mult=[]

    while i < len(nums):
        if nums[i]%n==0:
            mult = mult + [nums[i]]
        i=i+1
     
    return mult