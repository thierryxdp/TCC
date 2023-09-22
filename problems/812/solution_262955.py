def retira_pontuacao(frase):
    """
    Essa função recebe uma frase e retorna ela sem pontuações;
    str -> str
    """
    pontos = ".,:;-?!"
    for v in frase:
        if v in pontos:
            frase = frase.replace(v, ' ')
    return frase