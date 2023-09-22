def lingua_p (palavra):
    '''Função que recebe uma palavra (em português) e retorna esta mesma
palavra traduzida para a língua do P. A tradução para a língua do P insere a
sequência de letras p mais a vogal original após cada vogal.'''
    #str -> str
    palavra = list(palavra.lower())
    i = 0
    for letra in palavra:
        if letra in 'aáàãeéiíoóõuú':
            concatena = 'p' + letra
            palavra.insert(palavra.index(letra, i) + 1, concatena)
        i += 1
    palavra_final = ''.join(palavra)
    return palavra_final