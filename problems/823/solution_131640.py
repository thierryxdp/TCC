def faltante(lista):
    
    """Funçao que recebe uma lista 'L' de tamanho N-1 contendo numeros inteiros(nao repetidos) de 1 a N
    e retorna o numeor inteiro x que pertence ao intervalo [1,N] mas que nao pertence a lista de entrada L"""
    
    proximo = 0
    
    if 1 not in lista:
        
        return 1
    
    elif lista[-1] != lista[-2]+1 :
        
        return lista.index(lista[-1])+1
    
    else:
        
        while proximo < len(lista)-1:
            
            if lista[proximo]+1 != lista[(proximo)+1]:
                
                 x = lista.index(lista[proximo]) + 2
            proximo = proximo + 1
            
        return x