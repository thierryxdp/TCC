def lingua_p(p):
    linguap=''
    for indice in range(len(p)):
        if p[indice] in 'aeiou':
            linguap = p[indice] + 'p'
        else:
            linguap = linguap+p[indice]
    return linguap