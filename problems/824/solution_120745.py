def cons(palavra):
    vogais = 'AEIOUaeiou'
    for letra in palavra:
        if letra not in vogais:
            print(letra.upper())
        else:
            print(letra)