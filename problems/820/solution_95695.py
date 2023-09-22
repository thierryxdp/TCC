def posLetra(frase, letra, numero):
    """Funcao que recebe como entrada uma string, uma letra e um numero
    inteiro e retorna a posicao da letra na string referente ao numero de
    ocorrencia informado."""
    if str.count(frase,letra)>=numero:
        n=0
        vezes=0
        while vezes<ocorrencia:
            posicao = str.index(frase,letra,n)
            n = posicao + 1
        return posicao
    else:
        return -1