def filtra_pares(num):
    if num[0] %2 == 0:
         pri =(num[0],)
            
    elif num[1] %2 ==0:
        seg = (num[1],)
        
    elif num[2] %2 ==0:
        ter = (num[2],) 
        
    elif num[3] %2 ==0:
        quat = (num[3],)    
    return pri, seg, ter, quat