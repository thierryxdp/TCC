def filtraMultiplos(conjunto,n):
    
    numero= []
    count= 0
    
    while count < len(conjunto):
        if conjunto[count] % n == 0:
            
            numero.insert(count,conjunto[count])
            count = count +1
                          
    return numero