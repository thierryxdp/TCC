def lingua_p(p):
    linguap=''
    for indice in range(len(p)):
        if indice in 'aeiou':
            linguap = linguap + 'p'
        else:
            linguap = linguap + p[indice]
    return linguap