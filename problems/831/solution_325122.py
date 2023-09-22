def lingua_p(palavra):
    p=""
    for i in range(len(palavra)):
        if palavra[i] in "aeiou":
            p = p + "p" + palavra[i]
    return p