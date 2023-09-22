def subst_pontuacao(frase):
    '''retorna uma string de uma frase onde todos os caracteres de pontuacao tenham se tornado caracteres de espaco; str -> str'''
    novafrase = ''
    caractere = 0
    while caractere < len(frase):
        if not(frase[caractere] in '.!?,-:;'):
            novafrase = novafrase + frase[caractere]
        else:
            novafrase = novafrase + ' '
        caractere = caractere + 1    
    return novafrase




def inverte(frase):
    '''dada uma frase em string, retorna outra frase com a ordem de palavras invertida; str -> str'''
    lista_palavras = subst_pontuacao(frase.split(' ',len(frase)))
    list.reverse(lista_palavras)
    espaco = ' '
    frase_invertida = espaco.join(lista_palavras)
    return frase_invertida