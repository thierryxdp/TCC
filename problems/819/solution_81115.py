def filtraMultiplos(nums,n):
    '''funcao que filtra os multiplos de n;
    list,int -> list'''
    b=[]
    i = 0
      
    while i < len(n):
        
        if nums[i] % n ==0:
            b.append(nums[i])
                    
        i=i+1
        
    return b