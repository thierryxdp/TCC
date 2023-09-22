def lingua_p(palavra):
    palavra_nova=''
    i=0
    for letra in palavra:
        if letra in 'aeiou':
        	palavra_nova=palavra_nova+palavra[i]+'p'+letra
        i=i+1
    return palavra_nova