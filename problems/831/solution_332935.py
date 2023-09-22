def lingua_p(palavra):
    '''Traduz uma palavra para a língua do P
    entrada: str
    saída: str
    '''
    papalapavrapa=''
    e=0
    i=0
    palavra.lower()
    for letra in palavra:
        if letra in 'aeiou':
            papalapavrapa=papalapavrapa + palavra[e:i+1]+'p'
            e=i
        i=i+1
    papalapavrapa= papalapavrapa+ palavra[e:]
    return papalapavrapa