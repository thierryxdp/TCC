def lingua_p(palavra):
    vogais = 'AEIOUaeiou'
    palavras = palavra.split('a') 
    for i in vogais:        
        palavra = palavra.replace(i, 'p')
    return palavras