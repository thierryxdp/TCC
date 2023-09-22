def lingua_p(palavra):
    P=''
    for letra in palavra:
        if letra in 'aeiou':
            P=P+letra+'p'+letra
        else:
            P=P+letra
    return P