def lingua_p(palavra):
    
    traducao = ''
    str.lower(palavra)
    for letra in palavra:
        if letra in 'aeiou':
            letra_p = letra + 'p' + letra
            traducao += letra_p
        else:
            traducao += letra
    return traducao