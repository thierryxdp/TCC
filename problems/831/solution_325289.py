def lingua_p(palavra):
    """coment"""
    s=""
    for letra in palavra:
        if letra in "aeiouAEIOU":
            letra+="p"
            letra+=letra
        s+=letra
    return s