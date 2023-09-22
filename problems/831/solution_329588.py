def lingua_p(palavra):
    P="
    for letra in palavra:
        P+= letra
        if letra in 'aáãàâéêeíîioóõôúu':
            P+= 'p'+letra
            return P