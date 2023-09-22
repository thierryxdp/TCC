def lingua_p(palavra):
    """"""
    msg = ""
    i =0
    while i<len(palavra):
        if palavra[i] in "aeiou":
            msg = msg +"p"
        else:
            msg = msg+palavra[i]
        i+=1
    return msg