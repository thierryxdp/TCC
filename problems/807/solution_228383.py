def conta_frases (a):
    '''Função para contar o número de frases que aparecem no texto
str -> int'''
    
    x = str.replace (a,'!','?')
    z = str.replace (x,'?','.')
    y = str.replace (z,'...','.')
    return str.count (y,'.')