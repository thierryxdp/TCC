def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna esta mesma palavra traduzida para a língua do P.
    str -> str'''
    nova_lingua = ''
    for i in palavra:
        if i in 'aeiouáéíóúAEIOU':
            nova_lingua = nova_lingua + i + 'p' + i
        else: 
            nova_lingua = nova_lingua + i
    return nova_lingua