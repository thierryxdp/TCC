def filtraMultiplos(nums,n):
    """funcao que determina que numeros, contidos em
    uma lista (nums), são multiplos um numero(n). E 
    retorna uma lista com os multiplos na ordem que
    eles aparecem.
    entrada:list,int
    saida:list"""
    i=0
    mult=[]

    while i < len(nums):
        if nums[i]%n==0:
            mult = mult + [nums[i]]
        i=i+1
     
    return mult