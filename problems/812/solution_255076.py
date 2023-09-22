def retira_pontuacao(frase):
    '''
        Função que, dada uma frase, retorne a frase sem pontuação.
        Str => Str
    '''
    frase = frase.replace("-", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    return frase