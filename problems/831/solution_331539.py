def lingua_p(palavra):
    '''função que, dada uma palavra, retorna a
    mesma palavra traduzida para a língua do P,
    ouseja, após cada vogal é adicionada a letra 
    p mais a vogal original.
    str -> str'''
    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            palavra = str.replace(palavra,letra,letra + 'p' + letra,1)
    return palavra