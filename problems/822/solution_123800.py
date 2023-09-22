def repetidos(lista:list)->int:
    """ A função recebe como entrada uma lista de números, e retorna o número de vezes que um elemento da lista é igual ao elemento anterior"""
    indice = 0 
    quantidade_igual = 0
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            quantidade_igual = quantidade_igual + 1
        
        indice = indice + 1
    
    return quantidade_igual