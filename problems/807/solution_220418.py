def conta_frases(frase):
    '''função que conta o número de frases dado um texto
    valor de entrada: str
    valor de saída: int'''
    frase=frase.replace('...','trespontos')
    frase=frase.replace('!','exclamacao')
    frase=frase.replace('?','interrogacao')
    frase=frase.replace('.', 'ponto')
    resultadosoma= frase.count('ponto') + frase.count('exclamacao') + frase.count('interrogacao')+ frase.count('trespontos')
    if frase.count('ponto')>0 and frase.count('trespontos')>0:
         return resultadosoma-1
    else:
        return resultadosoma