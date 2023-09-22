def lingua_p(palavra):
for letra in palavra:
    P+=letra
    if letra in 'aáâãàéêeíîioóôõúu':
        P+='p'+letra
return P