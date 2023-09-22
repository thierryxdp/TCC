def repetidos(nums):
    """retorna o numero de vezes que um elemento da lista e igual ao anterior;
    list ->int"""
    i=1
    q=0
    
    while i<len(nums):
        if nums[i]==nums[i-1]:
            q=q+1
        i=i+1
    return q