def posLetra(string, letra, numero):
    """Recebe uma string, uma letra e um número que indica a ocorrência 
    desejada e retorna em que posição da string a ocorrência da letra está.
    Caso exista menos ocorrências da letra do que a ocorrência pedida, a 
    função retorna -1"""
    indice = 0
    ocorrencia = 0
    while indice < len(string):
        if string[indice] == letra:
            ocorrencia+=1
            if ocorrencia == numero:
                return string.index(string[indice], indice)
        indice+=1
    else:
        return -1