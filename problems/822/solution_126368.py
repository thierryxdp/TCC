def repetidos(lista):
    '''
    funcao que recebe uma lista
    e retorna o numero de vezes que um elemento da lista
    e igual ao elemento anterior
    list -> int
    '''
    contador = 0
    i = 0
    
    while i < len(lista):
        
        
        if lista[i] == lista[i+1]:
           	contador +=1
            
  
           
            
        return contador