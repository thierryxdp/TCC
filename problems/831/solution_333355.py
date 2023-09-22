def lingua_p (x):
    vogal=''
    for letra in x:
        if letra in 'AEIOUaeiouÁÉÍÓÚáéíóúÃÕãõ':
             vogal=vogal+letra+'p'+letra
        else:
            vogal+=letra
    return vogal