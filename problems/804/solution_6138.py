#Start your python function here
def filtra_pares(nums):
    """filtra os elementos pares de uma dada tupla contendo 4 inteiros
    parametros: (a,b,c,d) -> tupla
    retorna: tupla"""
    
    pares = ()
    
    if nums[0]%2 == 0:
        pares += (nums[0],)
        
    if nums[1]%2 == 0:
        pares += (nums[1],)
        
    if nums[2]%2 == 0:
        pares += (nums[2],)
        
    if nums[3]%2 == 0:
        pares += (nums[3],)
        
    return pares
    
    return pares