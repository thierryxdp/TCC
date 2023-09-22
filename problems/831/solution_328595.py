def lingua_p(palavra):
    """"""
    msg = ""
    i =0
    while i<len(palavra):
        if palavra[i] in "aeiouáéíóúAEIOU":
            msg = msg +palavra[i]+"p"+palavra[i]
        else:
            msg = msg+palavra[i]
        i+=1
    return msg