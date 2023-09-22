def uppCons(frase):
    vogais = 'aeiou'
    palavra = input('Digite uma palavra: ')
    while letra in palavra:
        if letra in vogais:
            return (letra.upper())