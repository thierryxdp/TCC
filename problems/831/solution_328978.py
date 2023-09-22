def lingua_p(palavra):
    P = ''
    for letra in palavra:
        if letra == 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstuvwxyz':
            P = P + letra
        else letra != 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstuvwxyz':
                P = P + letra + 'p' + letra
        return P