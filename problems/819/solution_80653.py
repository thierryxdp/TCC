def filtraMultiplos(nums,n):
    '''funcao que filtra os multiplos de n;
    list,int -> list'''
    
    i = 0
    multiplos = [nums]
    
    while nums[i] / n:
        multiplos = multiplos + list.insert(multiplos,i,nums[i])
        
    i = i + 1
        
    return multiplos