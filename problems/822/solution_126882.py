def repetidos(nums:list)-> int:
    """Recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior"""
    rept=0
    i=0
    while 0<len(nums):
        if nums[i]==nums[i-1]:
            rept=rept+1
        i=i+1
    return rept