def lingua_p(palavra):
    vogais = 'AEIOUaeiou'
    palavras = palavra.split(vogais) 
    for i in vogais:        
        palavras = palavras.append(i, 'p')
    return palavras