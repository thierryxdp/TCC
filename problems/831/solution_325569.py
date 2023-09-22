def lingua_p(p):
    str.lower(p)
    vogais='aeiouáéíóú'
    for i in vogais:
        if i in p:
            p=str.split(p,i)
            p=(i+'p'+i).join(p)
    return p