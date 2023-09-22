def lingua_p (palavra):
    '''função que recebe uma palavra e a traduz para a lingua do p, que após cada vogal da palavra insere a sequência
    p + vogal.
    str -> str'''
    
    vogais = 'aeiouáéíóúâêôãõ'
    posicao = 0
    palavra_p = palavra[:]
    
    for letra in palavra[posicao:]:
        if letra.lower() in vogais:
            palavra_p = palavra[0:posicao+1] + 'p' + letra + palavra[posicao+1:]
        posicao = posicao + 1
    return palavra_p