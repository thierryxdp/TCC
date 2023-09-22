def uppCons(f):
    '''transforma todas as cosoantes na frase(f)em maiúsculas, enquanto mantém todos
    os outros caracteres como era orginalmente'''
    i = 0
    frasemudada = f
    while i < len(f):
        if f[i] in 'BCDFGHJKLMNPQRSTVXYWZbcdfghjklmnpqrstvxywz':
            frasemudada[i].upper
        i = i+1
    return frasemudada[1].upper