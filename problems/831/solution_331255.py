def lingua_p(plv):
    """
    Ao inserir uma palavra, retornará ela para
    a língua do P.
    str->str.
    """
    menor=str.lower(plv)
    letras=list(menor)
    traducao=""
    for consoante in letras:
        if consoante not in "zxcvbnmsdfghjklqwrtyp":
            traducao=traducao+consoante+"p"+consoante
        else:
            traducao=traducao+consoante
    return traducao