def lingua_p (palavra):
    '''função que recebe uma palavra e a traduz para a lingua do p, que após cada vogal da palavra insere a sequência
    p + vogal.
    str -> str'''
    
    vogais = 'aeiouáéíóúâêôãõ'
    palavra_p= palavra[:]
    
    for letra in palavra:
        if letra.lower() in vogais:
            palavra_p = palavra[:palavra.index(letra)+1] + 'p' + letra + palavra[palavra.index(letra)+1:]
    return palavra_p