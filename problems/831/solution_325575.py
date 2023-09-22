def lingua_p(palavra):
    '''Função que dado uma palavra ,retorna essa palavra escrita na lingua do p.
    str->str'''
    vogais=['a','e','i','o','u']
    soma=''
    for letra in palavra:
        if letra in vogais:
            soma=soma + 'p' + letra + 'p'
        else:
            soma=soma + letra
    return soma