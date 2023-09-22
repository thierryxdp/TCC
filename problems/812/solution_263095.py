def retira_pontuacao(frase):
    """Tem como objetivo receber uma frase e retornar
    essa mesma frase sem as pontuações.
    str > str"""
    import re
    out = re.sub(r'[^\w\s]','',frase)
    return (out)