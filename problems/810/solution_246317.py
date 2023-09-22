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


def inverte(texto):
    texto = retira_pontuacao(texto)
    texto = texto.lower()
    separadas = texto.split()
    separadas1 = list(reversed(separadas))
    resultado = ' '.join(separadas1)
    return resultado