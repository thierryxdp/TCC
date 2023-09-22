def lingua_p(p):
    '''funçao que receba uma palavra em portugues e retorna
    esta mesma palavra traduzida para a lingua do P; str->str'''
    x=palavra.lower()
    y=''
    vogais='aeiouàáãéêíóúõô'
    for elem in x:
        y=y+elem
        if elem in vogais:
            y=y+´p´+elem
    return y