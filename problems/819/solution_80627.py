def filtraMultiplos(nums,n):
    '''funcao que filtra os multiplos de n;
    list,int -> list'''
    
    i = 0
        
    while i < n:
        
        if nums[i] / n:
            nums = nums + nums[i]
        
        i=i+1
        
    return nums