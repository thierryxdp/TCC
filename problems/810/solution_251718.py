def inverte ( frase):
    """ substitue travessão, virgula, dois pontos, ponto e virgula, além da pontuacao de encerramento de frase, por espaço """
    frase1= str.split (frase)
    frase2= frase1 [::-1]
    return frase2