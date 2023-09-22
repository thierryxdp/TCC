def conta_frases(frase):
    '''função que conta frases permitindo uso de reticencias, 
    interrogações e exclamação apenas no final delas'''
    interrogacoes = str.count(frase,'?')
    exclamacoes = str.count(frase,'!')
    reticencias = str.count(frase,'...')
    ponto_final = max(str.count(frase,'.') - reticencias,0)
    return interrogacoes + exclamacoes + reticencias + ponto_final