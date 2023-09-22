def filtraMultiplos(nums,n):
    '''funcao que filtra os multiplos de n;
    list,int -> list'''
    
    i = 0
      
    while i < n:
        
        if nums[i] / n:
            return nums
        
        i=i+1
        
    return nums