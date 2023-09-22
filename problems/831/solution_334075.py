def lingua_p(palavra):
    nova=palavra.lower()
    a=1
    for letra in nova:
        if letra in 'aeiou':
            nova=nova[0:a]+'p'+letra+nova[a:]
            a=a+3
        else:
            a=a+1