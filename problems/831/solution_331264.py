def lingua_p(palavra):
    letras=''
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            letra=letra+'p'
        letras=letras+letra
    return letras