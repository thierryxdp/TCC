def filtra_pares(tupla):
    ''' funcao que a partir de uma tupla retorna outra tupla com elementos pares da anterior 
        tup(int,int,int,int) --> tup(int,int,int,int) '''
    
    n1 = tupla[0]
    n2 = tupla[1]
    n3 = tupla[2]
    n4 = tupla[3]
    
    if (n1%2 == 0):
        
        if (n2%2 == 0):
            return tupla[0] + tupla[1]
        
        elif (n3%2 == 0):
            return tupla[0] + tupla[2]
        
        elif (n4%2 == 0):
            return tupla[0] + tupla[3]
        
        elif ((n2%2 == 0) and (n3%2 == 0)):
            return tupla[0] + tupla[1] + tupla[2]
        
        elif ((n2%2 == 0) and (n4%2 == 0)):
            return tupla[0] + tupla[1] + tupla[3]
        
        elif ((n3%2 == 0) and (n4%2 == 0)):
            return tupla[0] + tupla[2] + tupla[3]
        
        elif ((n2%2 == 0) and (n3%2 == 0) and (n4%2 == 0)):
            return tupla[0] + tupla[1] + tupla[2] + tupla[3]
        
        else:
            return tupla[0]
    
    elif (n2%2 == 0): 
        
        if (n3%2 == 0):
            return tupla[1] + tupla[2] 
        
        elif (n4%2 == 0):
            return tupla[1] + tupla[3]
        
        elif ((n3%2 == 0) and (n4%2 == 0)):
            return tupla[1] + tupla[2] + tupla[3]
        
        else:
            return tupla[1]
    
    elif (n3%2 == 0):
        
        if (n4%2 == 0):
            return tupla[2] + tupla[3]
        
        else:
            return tupla[2]
    
    elif (n4%2 == 0):
        return tupla[3]