def lingua_p(palavra):
    '''função que, dada uma palavra, retorna a
    mesma palavra traduzida para a língua do P,
    ouseja, após cada vogal é adicionada a letra 
    p mais a vogal original.
    str -> str'''
    palavra = str.lower(palavra)
    palavra2 = ''
    for letra in palavra:
        if letra in 'aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãõÃÕôÔ':
            palavra2 = palavra2 + letra + 'p' + letra
        else:
            palavra2 = palavra2 + letra
    return palavra2