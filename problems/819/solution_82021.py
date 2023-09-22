def filtraMultiplos(nums:list,n:int)->list:
    """Retorna todos os multiplos de um número n dada uma lista de números"""
    fmults=[]
    i=0
    while i<len(nums):
        if nums[i]%n==0:
            fmults=fmults+[nums[i],]
        i=i+1
    return fmults