def lingua_p(palavra):
    """função que recebe como parametro uma palavra e retorna a mesma palavra traduzida para lingua do p; str->str"""
    p=""
    for L in(palavra):
        p += L
        if L in "aàáêèéiìíoóòôùúu":
            p += "P"+ L
    return p