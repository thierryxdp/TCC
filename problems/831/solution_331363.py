def lingua_p (palavra: str)-> str:
    '''Retorna a palavra dada traduzida para a língua do P'''
    palavra2=''
    for e in palavra:
        palavra2 += e
        if e in 'aeiou':
            palavra2 = palavra2 + 'p' + e
    return palavra2