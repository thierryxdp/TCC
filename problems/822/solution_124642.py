def repetidos(lista):
    '''Recebe uma lista e retorna a quantidade de vezes que um 
       elemento é igual ao elemento anterior;
       list -> int'''
    
    pos = 0
    contador = 0
    
    while pos < len(lista)-1:
        
        pos += 1
        
        if lista[pos] == lista[pos-1]:
            
            contador += 1
 
    return contador