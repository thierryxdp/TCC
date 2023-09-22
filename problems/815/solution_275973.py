def inverso(frase):
    '''função que recebe uma frase e retorna a mesma ao contrário, sem sinais de pontuação e com as letras minúsculas. str --> str'''
    frase2 = frase.lower()

    frase2 = frase2.replace('.', ' ')
    frase2 = frase2.replace(',', ' ')
    frase2 = frase2.replace('...', ' ')
    frase2 = frase2.replace(':', ' ')
    frase2 = frase2.replace(';', ' ')
    frase2 = frase2.replace('?', ' ')
    frase2 = frase2.replace('!', ' ')
    frase2 = frase2.replace('_', ' ')

    listfrase = frase2.split()

    return ' '.join(listfrase[::-1])