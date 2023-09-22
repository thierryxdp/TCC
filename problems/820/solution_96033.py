def posLetra (string, letra, n_ocorrencia):
    """Recebe uma string, uma letra e um número e retorna
    a posição da ocorrência da letra de acordo com o número 
    escolhido.
    str, str, int -> int"""
    indice = 0
    posicao = []
    convertida = list(string)
    if str.count(string, letra) < n_ocorrencia:
        return -1
    else:
        while indice<len(string) and len(posicao)<n_ocorrencia:
            if string[indice] == letra:
                posicao+= [string[indice],]  
            indice += 1
        return indice -1