def lingua_p(palavra):
    palavra2=palavra.lower()
    a=1
    for letra in palavra2:
        if letra in 'aeiou':
            palavra2=palavra2[0:a]+'p'+letra+palavra2[a:]
            a=a+3
        else:
            a=a+1
        
    return palavra2