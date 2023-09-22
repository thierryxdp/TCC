def lingua_p(palavra):
    """A função retorna uma palavra traduzida na língua do P.
    str-->str."""
    
    trans = []
    vogais = 'aeiouáéíóú"
    for letra in (palavra):
        if letra in vogais:
            list.append(trans,letra +'p'+letra)
        else:
            list.append(trans,letra)
    return str.join('',trans)