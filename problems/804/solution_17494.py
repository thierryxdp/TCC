def filtra_pares(a,b,c,d):
    num=(a,b,c,d)
    final=(a,b,c,d)
    if num[2]%2==0:
        return a=num[2]
    
    elif num[4]%2==0:
       return b=num[4]
    
    elif num[6]%2==0:
      return c=num[6]
    
    elif num[8]%2==0:
       return d=num[8]
    
    return final[0:]