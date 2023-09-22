def lingua_p(palavra):
    """traduz uma palavra x para a língua do p;
    string, -> string"""
    
    palavran = palavra.lower()
    r = []
    for i in range(len(palavra)):
        if palavran[i] in "a":
            list.append(r, palavran)
        else:
            list.append(r, palavran[i]+"p"+palavran[i])
    return "".join(r)