def lingua_p
p="
for letra in palavra:
    p+=letra
    if letra in 'aáâãàéêeíîioóôõúu':
        p+='p'+letra
    return p