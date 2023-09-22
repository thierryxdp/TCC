def retira_pontuacao ( frase):
    """ substitue travessão, virgula, dois pontos, ponto e virgula, além da pontuacao de encerramento de frase, por espaço """
    frase = frase.replace (',', '')
    frase = frase.replace ('.', '')
    frase = frase.replace (':', '')
    frase = frase.replace ('-', '')
    frase = frase.replace ('!', '')
    frase = frase.replace ('?', '')
    return frase