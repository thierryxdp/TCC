def filtraMultiplos(nums,n):
    """retorna os elementos de uma lista que são multiplos de um numero.
    (list,int->list)"""
    multiplos=[]
    indice=0
    while indice<len(nums):
        if (nums[indice]%n) == 0:
            multiplos.append(nums[indice])
            indice+=1
        else:
            indice+=1
    return multiplos