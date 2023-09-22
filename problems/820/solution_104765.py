def posLetra (string, letra, n_ocorrencia):
    '''Função que retorna a posição da ocorrência de uma
    determinada letra em uma string
    str, str, int -> int'''
    lista = [string, letra, n_ocorrencia]
    n_ocorrencia = 'n_ocorrencia'
    
    i = 0
    if i < n_ocorrencia:
        return -1
    elif letra in lista:
        return string.count('letra')