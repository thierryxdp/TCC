def uppCons(palavra):
    i = 0
    while i < len(palavra):
        if palavra[i] in 'AEIOUaeiou':
            palavra = palavra.replace(palavra[i], palavra[i].upper())
        i = i + 1
    return palavra