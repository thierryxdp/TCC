def lingua_p(palavra):
    """traduz uma palavra x para a língua do p;
    string, -> string"""
    
    palavra = palavra.lower
    r = []
    for i in range(len(palavra)):
        if palavra[i] != 'a,e,i,o,u':
            list.append(r, palavra)
        else:
            list.append(r, palavra[i]+"p"+palavra[i])
    return "".join(r)