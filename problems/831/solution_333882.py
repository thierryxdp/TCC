def lingua_p(palavra):
    vogais = 'AEIOUaeiou'
    palavras = palavra.split('A', 'E', 'I', 'O', 'U', 'a', 'e' , 'i', 'o', 'u') 
    for i in vogais:        
        palavra = palavra.replace(i, 'p')
    return palavras