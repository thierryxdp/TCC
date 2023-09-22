def lingua_p(palavra):
    menor=str.lower(palavra)
    letras=list(menor)
    traduz=""
    for consoante in letras:
        if consoante not in "zxcvbnmsdfghjklqwrtyp":
            traduz=traduz+consoante+"p"+consoante
        else:
            traduz=traduz+consoante
    return traduz