def invert(frase):
    """Dada uma frase retorna a mesma sem pontuação
    str -> str
    str -> str"""
    removePontos = retira_pontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removeEspacos = fraseMinuscula.strip()
    novaFraseSplit = removeEspacos.split()[::-1]
    novaFraseJoin = " ".join(novaFraseSplit)
    return novaFraseJoin