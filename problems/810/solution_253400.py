def retira_pontuacao(frase):
    """dada uma frase com caracteres de pontuação retorna a
    mesma frase com a pontuaçãi substituida por espaços"""
    import string
    y=string.punctuation
    for x in y:
        frase = frase.replace(x,' ')
    return(frase)
def inverte(frase):
    """dada uma frase restorna a mesma frase em ordem inversa"""
    import string
    novafrase = retira_pontuacao(frase)
    minusculo = str.lower(novafrase)
    separa = minusculo.split()
    reverte = reversed(separa)
    juntastring = ' '.join(reverte)
    return juntastring