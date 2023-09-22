def lingua_p(p):
    linguap=''
    for indice in range(len(p)):
        if p[indice] in 'aeiou':
            linguap = linguap + p[indice] + 'p'+p[indice]
        
    return linguap