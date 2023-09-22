def lingua_p(palavra):
    """ """
    nova= ""
    c=0
    
    for i in range(len(palavra)):
        if palavra[i] in "aeiouAEIOU":
            nova= nova +palavra[c:i+1] + "p"
            c=i
    return nova + palavra[-1]