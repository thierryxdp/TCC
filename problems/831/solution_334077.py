def lingua_p(palavra):
    p=palavra.lower()
    a=1
    for letra in p:
        if letra in 'aeiou':
            p=p[0:a]+'p'+letra+p[a:]
            a=a+3
        else:
            a=a+1
    return n