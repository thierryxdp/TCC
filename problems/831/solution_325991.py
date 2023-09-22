def lingua_p(palavra):
    """Essa função retorna uma palavra na lingua do p"""
    """str->str"""
    lp=""
    for i in range(0,len(palavra)):
        if palavra[i] in "aeiouéúíóá":
            lp=lp+palavra[i]+"p"+palavra[i]
        else:
            lp=lp+palavra[i]
    return lp