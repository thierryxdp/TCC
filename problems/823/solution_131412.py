def faltante(lista):
    ''' Função que, dado a lista de entrada de numeros inteiros e tamho N-1,
    retorna o numero int x que falta. Ou seja, não pertence a lista de entrada'''
    
    
    cont = 1
    
    while cont <= len(lista):
        if cont in lista:
            cont += 1
        else:
            return cont
            
    return cont