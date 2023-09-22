def lingua_p(p):
    '''funçao que receba uma palavra em portugues e retorna
    esta mesma palavra traduzida para a lingua do P; str->str'''
    m=palavra.lower()
    n=''
    vogais='aeiouàáãéêíóúõô'
    for elem in m:
        n=n+elem
        if elem in vogais:
            n=n+´p´+elem
    return n