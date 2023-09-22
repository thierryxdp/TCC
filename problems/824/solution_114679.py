def uppCons(f):
    '''transforma todas as cosoantes na frase(f)em maiúsculas, enquanto mantém todos
    os outros caracteres como era orginalmente'''
    i = 0
    f1 = ""
    while i < len(f):
        if f[i] in 'BCDFGHJKLMNPQRSTVXYWZbcdfghjklmnpqrstvxywz':
            f1 = f1 + f[i].upper
        else:
            f1 = f1 + f[i]
        i = i+1
    return f1