def lingua_p(palavra):
    P="
for letra in palavra:
    P+=letra
    if letra in 'aáâãàéêeíîioóôõúu':
        P+='p'+letra
    return p