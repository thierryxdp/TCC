def inverte(frase):
    """dada uma frase esta função retornará a frase invertida e sem pontuação.
          str -> str """
    removePontos = retira_pontuacao(frase)
    fraseM = removePontos.lower()
    removeEspacos = fraseM.strip()
    novaFSplit = removeEspacos.split()[::-1]
    novaFJoin = " ".join(novaFrSplit)
    return novaFeJoin