def retira_pontuacao(frase):
    """Tem como objetivo receber uma frase e retornar
    essa mesma frase sem as pontuações.
    str > str"""
    frase = str.split(frase,".","!",",")
    frase = str.split(frase,";",":","-")
    frase = str.split(frase,"?")
    frase = str.join(" ", frase)
    return frase