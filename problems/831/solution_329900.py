def lingua_p(palavra):
    """função que recebe como parametro uma palavra e retorna a mesma palavra traduzida para lingua do p; str->str"""
    P=""
    for L in palavra:
        P += L
        if L in "aàãáêèéiìîíoóòõôùúu":
            P += "p"+ L
    return P