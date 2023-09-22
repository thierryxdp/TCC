def lingua_p(palavra):
    """coment"""
    s=""
    for letra in palavra:
        if letra in "aeiouAEIOU":
            letra=l
            letra+="p"
            letra+=l
        s+=letra
    return s