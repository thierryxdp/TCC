def inverte ( frase):
    """ substitue travessão, virgula, dois pontos, ponto e virgula, além da pontuacao de encerramento de frase, por espaço """
    frase1= str.split (frase)
    frase2= frase1 [::-1]

def remove (frase2)
    frase2 = frase2.replace (',', ' ')
    frase2 = frase2.replace ('.', ' ')
    frase2 = frase2.replace (':', ' ')
    frase2 = frase2.replace ('-', ' ')
    frase2 = frase2.replace ('!', ' ')
    frase2 = frase2.replace ('?', ' ')
    return frase2