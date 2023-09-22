def lingua_p(palavra):
    vogais = 'aeiou'
    for i in range(len(palavra)):
        if palavra[i] in vogais:
           nova = palavra.replace(palavra[i],(palavra[i]+'p'+palavra[i]))
    return nova