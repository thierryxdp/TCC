def lingua_p(p):
    """Dada uma palavra "p", em portugues, retorna traduzida na 
    lingua do P
    str -> str"""
    p = str.lower(p)
    vogais = "aeiouáàãâéêíóôõú"
    traduz = ""
    for l in p:
        if l in vogais:
            traduz = traduz+l+"p"+l
        else:
            traduz = traduz+l
    return traduz