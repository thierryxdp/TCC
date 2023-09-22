def lingua_p(palavra):
    """função que recebe como parametro uma palavra e retorna a mesma palavra traduzida para lingua do p; str->str"""
    traduz=""
    for L in(palavra):
        traduz += L
        if L in "aàáêèéiìíoóòôùúu":
            traduz += "traduz"+ L
    return traduz