def lingua_p(palavra):
    """retorna a palavra traduzida para a lingua do P;
    str -> str"""
    pmin=str.lower(palavra)
    pp=''
    for x in pmin:
        if x not in 'bcçdfghjklmnpqrstvwxyz':
            pp=pp+x+'p'+x
        else:
            pp=pp+x
            
    return pp