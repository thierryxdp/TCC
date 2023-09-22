def inverte(frase):
    """
        Dada uma frase esta função retornará a frase invertida e sem pontuações.
        Exemplo: "Nossa, como eu gosto de chocolate."
        Retorna: "chocolate de gosto eu como nossa"
        str -> str
        Parâmentros:
        Entrada: frase 
        Returna: frase sem pontuaçao e invertida 
    """
    removePontos = tira_pontuacao(frase)
    fraseMinuscula = removePontos.lower()
    removeEspacos = fraseMinuscula.strip()
    novaFraseSplit = removeEspacos.split()[::-1]
    novaFraseJoin = " ".join(novaFraseSplit)
    return novaFraseJoin