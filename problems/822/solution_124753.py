def repetidos(lista):
    ''' Função que dada uma lista de números, retorna o 
    número de vezes que um elemento da lista for igual ao
    seu antecessor.
    Entrada: list
    Retorno: int '''
    
    repeticoes = 0
    indice = 1
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            repeticoes += 1
        indice += 1
        
    return repeticoes