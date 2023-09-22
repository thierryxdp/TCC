def lingua_p(palavra):
    ''' funcao que recebe uma palavra em portugues e a traduz para a lingua p. str --> str'''
    nova_palavra= ''
    for letra in palavra:
        if letra in 'aeiou':
            nova_palavra += letra + 'p' + letra
        else:
            nova_palavra += letra
    return nova_palavra