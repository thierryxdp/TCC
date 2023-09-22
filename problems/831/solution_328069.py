def lingua_p(p):
    indice = 0
    lingua_p=''
    for indice < len(p):
        if p in 'aeiou':
            lingua_p = lingua_p + 'p'
        else:
            lingua_p = lingua_p + p
    return lingua_p