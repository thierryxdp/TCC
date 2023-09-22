def uppCons(frase):
    '''Funcao que dada uma frase, retorna a frase com todas as consoantes em caixa alta.
as demais letras (vogais) aparecem no retorno em caixa normal "baixa"
    str -> str'''
    posicao = 0
    vogais = 'aeiouãáéíóôâú'
    fraseResposta = ''

    while posicao < len(frase):
        if frase[posicao] not in vogais:
            fraseResposta += frase[posicao].upper()
            posicao = posicao + 1

        else:
            fraseResposta = fraseResposta + frase[posicao]
            posicao = posicao + 1

    return fraseResposta