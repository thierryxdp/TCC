def filtraMultiplos(nums,n):
    multiplos=[]
    indice=0
    while indice<len(nums):
        if (nums[indice]%n) == 0:
            multiplos.append(nums[indice])
            indice+=1
    return multiplos