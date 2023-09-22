def filtraMultiplos(nums,n):
    '''funcao que filtra os multiplos de n;
    list,int -> list'''
    
    i = 0
    nums = []
    multiplos = []
    
    while i < n:
        
        if nums[i] / n == True:
           	multiplos = multiplos + nums[i]
        
        i = i+1
        
    return multiplos