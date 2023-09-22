def conta_frases(text):
    '''Função que calcula o numero de frases dentro de um texto, text, a partir do numero de 
    pontos finais, exclamações, interrogaões e reticências. str->int'''
    p=str.count(text,'.')//3
    i=str.count(text,'?')
    e=str.count(text,'!')
    r=str.count(text,'...')
    return p+i+e+r