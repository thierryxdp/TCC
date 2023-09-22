def conta_frases(texto):
    '''Função que dado um texto em uma string,retorna a quantidade de frases no texto.string->int'''
    texto=texto.replace('...','.')
    return str.count(texto,'?')+str.count(texto,'!')+str.count(texto,'...')+str.count(texto,'.')