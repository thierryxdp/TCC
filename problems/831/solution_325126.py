def lingua_p(palavra):
    p=""
    for i in range(len(palavra)):
        if palavra[i] in "aeiouáéíó":
            p = p + palavra[i] + "p" + palavra[i]
        else:
            p = p + palavra[i]
            
    return p