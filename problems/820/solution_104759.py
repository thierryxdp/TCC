def posLetra (string, letra, n_ocorrencia):
    '''Função que retorna a posição da ocorrência de uma
    determinada letra em uma string
    str, str, int -> int'''
    lista = [string, letra, n_ocorrencia]
    
    if letra in lista:
        return string.count('letra')
    elif letra < n_ocorrencia:
        return -1