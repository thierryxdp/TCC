def posLetra(string, letra, numero):
    '''Retorna a posição da string em qual ocorrência da letra recebida
    está, caso n, caso não encontrda retorna -1 
    string, string int -> int'''
    indice = 0
    ocorrencia = 0
    while indice < len(string):
        if string[indice] = letra:
            ocorrencia = indice
        else:
            ocorrencia = -1
        indice += 1
    return ocorencia