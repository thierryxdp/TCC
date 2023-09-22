def retira_pontuacao(frase):
    """dada uma frase com caracteres de pontuação retorna a
    mesma frase com a pontuaçãi substituida por espaços"""
    import string
    y=string.punctuation
    for x in y:
        frase = frase.replace(x,' ')
    return(frase)