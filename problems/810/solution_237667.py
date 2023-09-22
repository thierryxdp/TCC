def invert(frase):
    """Dada uma frase retorna a mesma sem pontuação
    str -> str
    str -> str"""
    removePontos = retira_pontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removeEspacos = fraseMinuscula.strip()
    novafrasesplit = removeEspaços.split()[::-1]
    novafrasejoin = " ".join(novafrasesplit)
    return novafrasejoin