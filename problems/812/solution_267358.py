def retira_pontuacao(frase):
    """dada uma frase com caracteres de pontuação retorna
    essa mesma frase com pontuação substituida por espaço"""
    import string 
    y=string.punctuation
    for x in y: 
        frase = frase.replace(x,' ')
    return(frase)