def lingua_p(p):
    lingua_p=''
    for x < len(p):
        if x in 'aeiou':
            lingua_p = lingua_p + 'p'
        else:
            lingua_p = lingua_p + p
    return lingua_p