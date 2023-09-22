def lingua_p(palavra):
    i=0
    palavra_nova=''
    for letra in palavra:
        if letra in 'aeiou':
        palavra_nova=palavra[0:i]+letra+'p'+letra
        i=i+1
    return palavra_nova