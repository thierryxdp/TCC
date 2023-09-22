def lingua_p(p):
    linguap=''
    for indice in range(len(p)):
        if indice in 'aeiou':
            linguap = linguap + 'p'
    return linguap