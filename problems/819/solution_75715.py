def filtra_multiplos(lista,n):
    """funcao que calcula e retorna os numeros da lista fornecida que 
       sao multiplos do numero n fornecido
       
       lista, int -> lista
    """
    i = 0 
    multiplos = []
    
    while i<len(lista):
        if lista[i] % n == 0:
            list.append(multiplos, lista[i])
            
        i = i+1 
        
        
    return multiplos