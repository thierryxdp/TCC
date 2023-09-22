def lingua_p(palavra):
    i=0
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            letra=str.lower(letra)
        palavra_nova=palavra[i]+'p'+letra
        i=i+1
    return palavra_nova