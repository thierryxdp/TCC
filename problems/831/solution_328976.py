def lingua_p(palavra):
    P = ''
    for letra in palavra:
        if letra == 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstuvwxyz':
            P = P + letra
        elif letra != 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstuvwxyz':
            P = P + letra + 'p' + letra
        return P