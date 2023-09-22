def lingua_p(palavra):
    p=''
    for letra in palavra:
        p+= letra
        if letra in 'aáãâéêeíîioóõôúu':
            p+= 'p'+letra
    return p