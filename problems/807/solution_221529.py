def conta_frases(texto):
    '''Dado um texto, conta o numero de frases no mesmo, usando como parametro para determinação das frases o ponto final, ponto de exclamação,
    ponto de interrogação e reticências.str->int'''
    frase=texto.split('...')
    frase2=texto.split('!')
    frase3=texto.split('.')
    frase4=texto.split('?')
    if '...' in texto:
        return (len(frase)-1-(texto.count('...')*3))+(len(frase2)-1)+(len(frase3)-1)+(len(frase4)-1)
    else:
        return (len(frase)-1)+(len(frase2)-1)+(len(frase3)-1)+(len(frase4)-1)