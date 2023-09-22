def faltante(lista):
    """Função que dada uma lista com N-1 elementos inteiros, retorna o 
    elemento que está faltando no intervalo
    
    Parameters:
    lista: Lista de elementos inteiros numerados de 1 a N
    
    Returns:
    Retorna o elemento faltante no intervalo
    list -> int
    """
    list.sort(lista)
    if 1 not in lista:
        return 1
    if lista[-1]<len(lista)+1:
        return len(lista)+
    i=0
    faltante = 0
    while i < len(lista)-1:
        if lista[i+1]-lista[i]>1:
            faltante=faltante+lista[i]+1
        i+=1
    return faltante