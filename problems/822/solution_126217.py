def repetidos(lista):
    """Função que dada uma lista retorna o número de vezes que um elemento da lista é igual ao elemento anterior"""
    """lista -> int"""
    
    rep = 0
    i = 0
    
    for i range (len(lista)-1):
        if lista[i] == (lista[i+1]):
            rep = rep + 1
        i = i + 1
    return rep