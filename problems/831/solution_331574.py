def lingua_p(palavra):
    palavra2=''
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            palavra2= palavra2 + letra +'p'+letra
        else:
            palavra2= palavra2+letra
    return palavra2