def posLetra (texto, letra, ocorrencia):
    '''função que recebe um texto e retorna a posição da ocorrência de uma letra nesse texto.
    str, str, int -> int'''
    
    indice = 0
    lista = []
    
    while indice < len(texto):
        if letra == texto[indice]:
            list.append(lista, letra)
        indice = indice + 1
    return lista[ocorrencia-1]