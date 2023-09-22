def repetidos(lista):
    """Função que, dada uma lista de números, retorna o número de vezes que um elemento da lista é igual ao elemento anterior; lista->int"""
    
    indice = 0
    contagem = 0
    
    while indice < len(lista):
        if lista[indice] == lista[indice+1]:
            contagem = contagem+1
        indice = indice+1
    return contagem