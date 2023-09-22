def inverte(frase):
    """Retornar uma frase incial, entretanto toda minuscula, sem pontuações e com a ordem inversa;
    string - > string"""
    frases = retira_pontuacao(frase).lower().split(" ")[::-1]
    return " ".join(frases)