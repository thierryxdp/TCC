def lingua_p(palavra):
    """Recebe uma palavra e retorna ela mesma traduzida para a
    língua do P;
    str -> str"""
    vogais = "aáâàãäeéêèëiíîìïoóôòõöuúûùü"
    i = 0
    for letra in palavra:
        if letra.lower() int vogais:
            palavra = palavra[:i+1] + "p" + palavra[i:]
         	i += 2
        i += 1
    return palavra