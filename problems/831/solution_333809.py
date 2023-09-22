str--> str
traduzido_p = []
contador = 0
for letra in list(palavra):
    if letra in 'aeiou':
        traduzido_p.append(letra + 'p' + letra)
    else:
        traduzido_p.append(letra)
return ''.join(traduzido_p)