def lingua_p (palavra: str)-> str:
    '''Retorna a palavra dada traduzida para a língua do P'''
    palavra3=''
    for i in range(len(palavra)):
        if palavra[i] in 'aeiou':
            palavra2 = palavra[:i+1] + 'p'+ palavra[i]
            palavra3 += palavra2
        i+=1
    return palavra2