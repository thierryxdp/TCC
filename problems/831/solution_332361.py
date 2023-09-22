def lingua_p(palavra):
    '''retorna a palavra dada traduzida para a língua do p, que adiciona p + vogal após a aparição de uma vogal
    str -> str'''
    nova_palavra = ''
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            nova_palavra += letra + 'p' + letra
        else:
            nova_palavra += letra
    return nova_palavra