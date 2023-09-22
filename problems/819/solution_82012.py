def filtraMultiplos(nums:list,n:int)->list:
    """Retorna todos os multiplosde um número n dada uma lista de números"""
    i=0
    mult=[]
    while i<len(nums):
        if n%nums[i]!=0:
            mult=mult+nums[i]
        i=i+1
    return mult