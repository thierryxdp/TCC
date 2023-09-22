def inverte(frase1):
    """str=>str"""
    frase_nova = str.split(retira_pontuacao(str.lower(frase1))," ")
    return str.join(" ",frase_nova[::-1])