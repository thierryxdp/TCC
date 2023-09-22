def inverte(frase):
    """dada uma frase esta função retornará a frase invertida e sem pontuação.
          str -> str """
    removepontos = retira_pontuacao(frase)
    fraseminuscula = removepontos.lower()
    removeEspacos = fraseminuscula.strip()
    nFraseSplit = removeEspacos.split()[::-1]
    nFraseJoin = " ".join(nFraseSplit)
    return nFraseJoin