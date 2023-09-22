def lingua_p(p):
    linguap=''
    for indice in range(len(p)):
        if p[indice] in 'aeiouéáú':
            linguap = linguap + p[indice] + 'p'+p[indice]
        else:
            linguap = linguap+p[indice]
    return linguap