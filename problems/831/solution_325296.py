def lingua_p(palavra):
    """coment"""
    s=""
    for letra in palavra:
        if letra in "aeiouAEIOU":
            l=letra
            letra+="p"
            letra+=l
        s+=letra
    return s