def uppCons(frase):
    ''' Funcao que recebe como entrada uma frase
    e retorna a mesma frase com todas as consoantes maiusculas'''
    a=''
    b=0
    while b<len(frase):
        if frase[b] in 'bcdfghjklmnpqrstvxwyz':
            a=a+ frase[b].upper()
        else:
            a= a + frase[b]
        b=b+1
    return a