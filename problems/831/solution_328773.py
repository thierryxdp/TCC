def lingua_p(palavra):
    """traduz uma palavra x para a língua do p;
    string, -> string"""
    
    pn = palavra.lower()
    r = []
    i = 0
    for i in range(len(palavra)):
        if pn[i] != "a" and pn[i] != "i" and pn[i] != "e"
            list.append(r, pn[i])
        else:
            list.append(r, pn[i]+"p"+pn[i])
    return "".join(r)