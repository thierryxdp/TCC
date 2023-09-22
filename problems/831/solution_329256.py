def lingua_p(palavra):
    palavra_nova=''
    i=0
    for letra in palavra:
        if letra in 'aeiou':
        	palavra_nova=palavra[:i]+letra+'p'+letra
    return palavra_nova