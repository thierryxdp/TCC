def lingua_p(palavra):
    i=0
    palavra_nova=''
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            letra=str.lower(letra)
        palavra_nova=palavra_nova+letra+'p'+letra
        i=i+1
    return palavra_nova