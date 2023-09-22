def filtraMultiplos(nums,n):
    '''funcao que filtra os multiplos de n;
    list,int -> list'''
    
    i = 0
    multiplos = []
      
    while i < n:
        
        if nums[i] / n:
            return nums[i]
        
        i=i+1
        multiplos = multiplos + nums[i]
        
    return multiplos