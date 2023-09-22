def conta_frases(frase):
    '''função que conta o número de frases dado um texto
    valor de entrada: str
    valor de saída: int'''
    
    resultadosoma= frase.count('.') + frase.count('!') + frase.count('?')+ frase.count('...')
    
    if frase.count('.')>0 and frase.count('...')>0:
         return resultadosoma-(frase.count('.')-(frase.count('...')*3))
    else:
        return resultadosoma