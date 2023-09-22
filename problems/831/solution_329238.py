def lingua_p(palavra):
    frase=''
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            letra=str.lower(letra)
        frase=letra+'p'+letra
    return frase