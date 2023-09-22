def conta_frases(texto):
    '''Dado um texto armazenado em uma string, conta o número de frases 
    que aparecem nesse texto. Cada frase precisa ser terminada com um ponto 
    final, de exclamação, de interrrogação ou tres pontos, sem repetição.
    str->int'''
    
    exc=str.replace(texto,'!','.')
    inter=str.replace(exc,'?','.')
    ret=str.replace(inter,'...','.')
    right=str.rstrip(ret)
    lista=str.split(right)
    
    
    return len(lista)