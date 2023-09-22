def lingua_p(palavra):
    '''Recebe como parâmetro uma palavra (em português) e retorne esta mesma
    palavra traduzida para a língua do P.
    str->str
    '''
    palavra.lower()
    aux='aiueo'
    linguap=''
    for x in range(len(palavra)):
        linguap.join(palavra[x])
        if palavra[x] in aux:
            linguap.join('p')
            linguap.join(palavra[x])
    return linguap