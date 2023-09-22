def retira_pontuacao(frase):
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