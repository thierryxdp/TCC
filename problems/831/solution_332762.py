def lingua_p(palavra):
    """..."""
    nf=''
    for letra in palavra.lower:
        nf+=letra
        if letra in "aeiou":
            nf+='p'+letra
    return nf