def uppCons(frase):
    '''Funcao que recebe uma frase e retorna esta frase com todas as
consoantes maiusculas e os demais caracteres exatamente iguais ao original'''
    FraseNova = ''
    i = 0
    while i < len(frase):
        caracter = frase[i]
        if caracter in 'bcçdfghjklmnpqrstvwxyz':
            caracter = caracter.upper()
        FraseNova = FraseNova + caracter
        i = i+1
    return FraseNova