def lingua_p(palavra):
    """..."""
    np=str.lower(palavra)
    nf=''
    for letra in palavra:
        nf+=letra
        if letra in "aeiou":
            nf+='p'+letra
    return nf