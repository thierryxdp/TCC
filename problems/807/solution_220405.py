def conta_frases(frase):
    '''função que conta o número de frases dado um texto
    valor de entrada: str
    valor de saída: int'''
    frase=frase.replace('...','trespontos')
    frase=frase.replace('!','exclamacao')
    frase=frase.replace('?','interrogacao')
    frase=frase.replace('.', 'ponto')
    frase=frase.replace(',','virgula')
    return frase.count('ponto') + frase.count('exclamacao') + frase.count('interrogacao')+ frase.count('trespontos')