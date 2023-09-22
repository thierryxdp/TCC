def filtraMultiplos(nums:list,n:int)->list:
    """Retorna todos os multiplosde um número n dada uma lista de números"""
    i=0
    while i<len(nums):
        if n%nums[i]!=0:
            fmults = fmults + (nums[i],)
        i=i+1
    return fmults