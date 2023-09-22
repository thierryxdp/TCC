def inverte(frase):
    """
    Dada uma frase esta função retornará a frase invertida e sem pontuações.
    Exemplo: "Nossa, como eu gosto de chocolate."
    Retorno: "chocolate de gosto eu como nossa"
    :param frase: str -> str
    :return: str -> str
    """
    removePontos = retira_pontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removeEspacos = fraseMinuscula.strip()
    novaFraseSplit = removeEspacos.split()[::-1]
    novaFraseJoin = " ".join(novaFraseSplit)
    return novaFraseJoin