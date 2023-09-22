def uppCons(frase):
    '''Função que dada uma frase, retorna a frase com todas as letras maiusculas: str -> str'''
    i = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            print(frase.upper[i])
            i += 1