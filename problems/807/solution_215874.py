def conta_frases(text):
    '''Função que calcula o numero de frases dentro de um texto, text, a partir do numero de 
    pontos finais, exclamações, interrogaões e reticências. str->int'''
    p=str.find(text,'.')
    i=str.find(text,'?')
    e=str.find(text,'!')
    r=str.find(text,'...')
    return p+i+e+r