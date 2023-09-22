def inverte (frase):
    """retorne a frase de entrada transcrita contendo as mesmas palavras da frase de entrada na ordem inversa"""
    def retira_pontuacao(frase):
    frase= frase.replace('!',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace(',',' ')
    frase= frase.replace('?',' ')
    return frase
    frase = frase.split()
    frase.reverse()
    return ' '.join(frase)