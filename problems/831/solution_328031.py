def lingua_p(palavra):
    """função que torna uma palavra em sua contraparte da lingua do P;
    str->str"""
    w=str.lower(palavra)
    x=list(w)
    pp=""
    for k in x:
        pp=pp+k
        if k in ("aáãàâeéêiíîoóõôuúû"):
            pp=pp+"p"+k
    return pp