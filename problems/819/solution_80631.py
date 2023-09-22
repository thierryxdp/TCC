def filtraMultiplos(nums,n):
    '''funcao que filtra os multiplos de n;
    list,int -> list'''
    
    i = 0
    multiplos = []
    
    while i < n:
        
        if nums[i] / n:
            multiplos = multiplos + nums[i]
        
        i = i+1
        
    return multiplos