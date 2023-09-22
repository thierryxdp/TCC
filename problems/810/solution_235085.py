def retira_pontuacao(frase):
    '''
        Função que retira a pontuação da frase..
        Str => Str
    '''
    frase = frase.replace("-", " ")
    frase = frase.replace("!", "")
    frase = frase.replace(",", "")
    frase = frase.replace(".", "")
    frase = frase.replace("?", "")
    frase = frase.replace(":", "")
    frase = frase.replace(";", "")
    return frase
def inverte(frase):
    '''
        Função que retorna uma frase com a ordem inversa das palavras.
    '''
    frase = frase.lower()
    frase = retira_pontuacao(frase)
    frase = frase.split(" ")
    frase = frase[::-1]
    frase = ' '.join(frase)
    return frase