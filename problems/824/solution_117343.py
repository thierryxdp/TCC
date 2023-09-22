def uppCons(frase):
    vogais = 'aeiou'
    palavra = input('Digite uma palavra: ')
    while frase in palavra:
        if frase in vogais:
            return (frase.upper())