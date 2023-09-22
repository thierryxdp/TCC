def lingua_p(p):
    linguap=''
    for indice in range(len(p)):
        if p in 'aeiou':
            linguap = linguap + 'p'
        else:
            linguap = linguap + p
            return linguap