def inverte ( frase):
    """ substitue travessão, virgula, dois pontos, ponto e virgula, além da pontuacao de encerramento de frase, por espaço """
    frase = frase.replace (',', ' ')
    frase = frase.replace ('.', ' ')
    frase = frase.replace (':', ' ')
    frase = frase.replace ('-', ' ')
    frase = frase.replace ('!', ' ')
    frase = frase.replace ('?', ' ')
    frase1= str.split (frase)
    frase2 = frase1 [1]
    frase3= frase1 [0]
    return str.lower (frase2 + " " + frase3)