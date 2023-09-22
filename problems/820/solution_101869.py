def posLetra(frase, letra, ocorrencia):
    '''Função que dada uma frase procura a letra dada com o número de
    ocorrência dado e retorna a posição da letra na frase, caso não
    ache retorna -1
    str, str, int -> int'''
    if str.count(frase, letra) >= ocorrencia:
        str1 = ''
        contador = 0
        while str1 != letra * ocorrencia:
            if frase[contador] == letra:
                str1 += letra
                posicao = contador
            contador += 1
        return posicao
    else:
        return -1