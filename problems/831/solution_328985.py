def lingua_p(palavra):
    palavra = str.lower(palavra)
    P = ''
    for letra in palavra:
        if letra in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            P = P + letra
        elif letra not in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            P = P + letra + 'p' + letra
    return P