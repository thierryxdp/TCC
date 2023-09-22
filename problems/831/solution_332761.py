def lingua_p(palavra):
    """..."""
    np=palavra.lower
    nf=''
    for letra in np:
        nf+=letra
        if letra in "aeiou":
            nf+='p'+letra
    return nf