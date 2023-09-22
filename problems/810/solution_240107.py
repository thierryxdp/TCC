def retira_pontuacao(frase):
    """retorna a frase substituindo todos caracteres de pontuação por espacos em branco"""
    frase= frase.replace('!',' ')
    frase= frase.replace(':',' ')
    frase= frase.replace(';',' ')
    frase= frase.replace('.',' ')
    frase= frase.replace('-',' ')
    frase= frase.replace(',',' ')
    frase= frase.replace('?',' ')
    return frase
def inverte (frase):
    """retorne a frase de entrada transcrita contendo as mesmas palavras da frase de entrada na ordem inversa"""
    frase= frase.split()
    frase.reverse()
    return ' '.join(frase)