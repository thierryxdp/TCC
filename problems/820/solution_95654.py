def posLetra(texto, letra, n):
    '''Calcula a posição da enésima ocorrência 
    de uma dada letra num dado texto. Se o número da
    ocorrência solicitada for maior do que as 
    existentes, retorna -1;
    str, str, int -> int'''
    
    if texto.count(letra) > n:
        return -1
    
    indice = 0
    ocorrencia = 0
    
    while indice < len(texto):
        if texto[indice] == letra:
            ocorrencia += 1
        if ocorrencia == n:
            return indice