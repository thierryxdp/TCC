def lingua_p(palavra):
    palavra_nova=''
    for letra in palavra:
        if letra in 'aeiou':
        	palavra_nova=palavra_nova+letra+'p'+letra
    return palavra_nova