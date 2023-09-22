def lingua_p(frase):
    i = 0
    for vogal in frase:
        if vogal in 'aeiou': 
            frase.replace(vogal+1,p)
    return frase