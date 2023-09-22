def posLetra(frase: str, letra:str, ocorrencias:int)-> int:
    """Essa função, dada uma string, uma letra e um número que indica
    ocorrência, retorna em que posição da string aquela ocorrência da 
    letra está""""
    #Utilizando dois contadores, um para o indice e outro quantas vezes a letra se repete
    i = 0
    posicao = 0
    while i < len(frase):
        #Dentro do laço while, se o indice da str for igual a letra, some 1 no contador posicao
        if frase[i] == letra:
            posicao = posicao + 1
            #Se o número de vezes que a letra se repete(posicao) for igual ao número de ocorrencias, retorne o indice dessa letra na string.
            if posicao == ocorrencias:
                ocorre = frase.index(frase[i], i)
                return ocorre
        i += 1
    else:
        return -1