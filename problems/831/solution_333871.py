def lingua_p(palavra):
    vogais = 'AEIOUaeiou'
    for i in vogais:        
        palavra = palavra.append(i, 'p')
    return palavra