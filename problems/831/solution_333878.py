def lingua_p(palavra):
    vogais = 'AEIOUaeiou'
    palavras = palavra.split(vogais) 
    for i in vogais:        
        palavra = palavra.replace(i, 'p')
    return palavras