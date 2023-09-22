def faltante(lista):
    """
    Função que recebe uma lista de N inteiros de 1 até N+1
    e retorna o número que falta para completar a lista
    """
    
    N=len(lista)+1
    
    Sn=((1+N)*N)/2
    
    return Sn - sum(lista)