def filtraMultiplos(nums,n):
    '''funcao que filtra os multiplos de n;
    list,int -> list'''
    
    i = 0
    multiplos = [nums]
    
    while nums[i] / n:
           	multiplos = nums[i]
        
    i = i + 1
        
    return multiplos