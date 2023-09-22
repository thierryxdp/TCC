def filtra_pares(tupla):
    '''Função que recebe uma tupla com quatro elementos
    e deve retornar uma nova tupla com apenas os elementos
    pares da tupla original;
    tupla -> tupla'''
    
    tupla_pares=()
    
    if((tupla[0]%2)==0):
        tupla_pares+=(tupla[0],)
        
    elif((tupla[1]%2)==0):
        tupla_pares+=(tupla[1],)
        
    elif((tupla[2]%2)==0):
        tupla_pares+=(tupla[2],)
        
    elif((tupla[3]%2)==0):
        tupla_pares+=(tupla[3],)
        
    return tupla_pares