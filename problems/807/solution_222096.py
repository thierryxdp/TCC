def conta_frases(texto):
    '''
        recebe um texto e retorna a quantidade de frases que ela contem
        entrata: string
        saida: inteiro
    '''
    qtd=0
    qtd=qtd+str.count(texto,'!')
    qtd=qtd+str.count(texto,'?')
    qtd=qtd+str.count(texto,'...')
    qtd=qtd+str.count(texto,'.')-(3*str.count(texto,'...'))
    return qtd