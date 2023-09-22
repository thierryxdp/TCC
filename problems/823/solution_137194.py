def somas(n):
    
    soma = 1

    
    while n >= 1:
        soma += n
        n -= 1
        
    
    
    return soma-1

def faltante(lista):
    '''
    função que recebe uma lista com N-1 inteiros numerados
    de 1 a N e retorna o número que esta faltando
    '''
    return somas(len(lista)) - sum(lista)