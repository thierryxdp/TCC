def lingua_p(palavra):
    '''função que realiza a tradução de uma palavra da língua portuguesa
    para a língua do P
    str -> str'''
    nova_palavra = ''
    for letra in palavra:
        if letra in 'aeiouAEIOU''':
            letra = letra + 'p'
        nova palavra = nova palavra + letra
    return nova_palavra