def conta_frases(texto):
    '''retorna o número de frases que aparecem no texto
    str->int'''
    teste1=str.count(texto,'.')
    teste2=str.count(texto,'!')
    teste3=str.count(texto,'?')
    teste4=str.count(texto,'...')
    
    if teste4>0:
        return teste1+teste2+teste3+teste4-3*teste4
    else: 
        return teste1+teste2+teste3+teste4