def conta_frases(frase):
    '''função que conta frases permitindo uso de reticencias, 
    interrogações e exclamação apenas no final delas'''
    interrogações = str.count(frase,'?')
    exclamações = str.count(frase,'!')
    reticencias = str.count(frase,'...')
    ponto_final = max(str.count(frase,'.') - reticencias),0)
    return interrogações + exclamações + reticencias + ponto_final