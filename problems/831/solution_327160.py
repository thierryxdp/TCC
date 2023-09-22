def lingua_p(palavra):
    '''Função que recebe uma palavra em português como entrada e 
    retorna a palavra traduzida para língua do p. A lingua do p insere a
    letra p após cada vogal e repete a vogal.
    str -> str'''
    n= str.lower(palavra)
    traducao= ''
    for x in n:
        if x in 'aeiouáãéêíóõôúû':
            traducao= traducao + x + 'p' + x
        else: 
            traducao= traducao + x
    return traducao