def lingua_p(palavra):
    P="
for letra in palavra:
    P+=letra
    if letra in 'aáâãàéêeíîioóôõúu':
        P+='P'+letra
    return P