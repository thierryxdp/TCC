def lingua_p(palavra):
    fraseNew = ''
    x = 0
    for i in 'aeiou':
        vogal = palavra [x]
        if vogal in 'aeiou':
            fraseNew  = fraseNew + 'p'
        #fraseNew = fraseNew + consoante
    return fraseNew