def lingua_p (palavra):
    '''função que recebe uma palavra e a traduz para a lingua do p, que após cada vogal da palavra insere a sequência
    p + vogal.
    str -> str'''
    
    palavra=palavra.lower()
    vogais = 'aeiouáéíóúâêôãõ'
    palavra_p= palavra[:]
    contador = 1
    
    for letra in palavra:
        if letra.lower() in vogais:
            palavra_p = palavra_p[:palavra_p.index(letra)+contador] + 'p' + letra + palavra[palavra.index(letra)+contador:]
            contador = contador + 1
    return palavra_p