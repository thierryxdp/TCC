def conta_frases(texto):
    '''Dado um texto armazenado em uma string, conta o número de frases 
    que aparecem nesse texto. Cada frase precisa ser terminada com um ponto 
    final, de exclamação, de interrrogação ou tres pontos, sem repetição.
    str->int'''
    
    return len(str.split(texto, '.' or'!'or'?'or'... '))-1