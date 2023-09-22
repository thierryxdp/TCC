def faltante(lista):
    '''Função que dada uma lista de números (lista)
    retorna o número que estiver faltando no intervalo numérico
    dado na lista.
    list[int]->int'''
    
    list.sort(lista)
    i=0
    
    if lista[0] != 1:
        return 1
    
    while i< len(lista)-1:
        if lista[i] +1 != lista [i+1]:
            return lista[i]+1
        i=i+1
        
    return lista [-1]+1