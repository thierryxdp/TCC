def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna esta mesma traduzida na
    lingua do p
    str -> str
    '''
    nova_palavra = ''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouéíóúá':
            nova_palavra = nova_palavra + palavra[i] + 'p' + palavra[i]
        else:
            nova_palavra = nova_palavra + palavra[i]
    return nova_palavra