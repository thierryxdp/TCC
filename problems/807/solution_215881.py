def conta_frases(text):
    '''Função que calcula o numero de frases dentro de um texto, text, a partir do numero de 
    pontos finais, exclamações, interrogaões e reticências. str->int'''
    p=str.count(text,'.')
    i=str.count(text,'?')
    e=str.count(text,'!')
    r=str.count(text,'...')
    if(r==0):
        return p+i+e+r
    elif(r!=0):
        return (p//3)+i+e+r
    elif(r==1):
        return i+e+r