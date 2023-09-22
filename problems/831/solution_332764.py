def lingua_p(palavra):
    """..."""
    np=str.lower(palavra)
    nf=''
    for letra in palavra:
        nf+=letra
        if letra in "aeiouáéíóúâêôã":
            nf+='p'+letra
    return nf