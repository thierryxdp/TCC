def conta_frases(texto):
    '''Retorna quantas frases aparecem
       no texto inserido; str->int'''
    divisor=str.partition(texto,'.')
    contagem=len(divisor)
    n1=contagem-2
    divisor2=str.partition(texto,'!')
    contagem2=len(divisor2)
    n2=contagem-2
    divisor3=str.partition(texto,'?')
    contagem3=len(divisor3)
    n3=contagem-2
    divisor4=str.partition(texto,'...')
    contagem4=len(divisor4)
    n4=contagem-2
    if '.' in texto==True:
        return n1
    if '!' in texto==True:
        return n2
    if '?' in texto==True:
        return n3
    if '...' in texto==True:
        return n4
    if '.' in texto==True and '!' in texto==True:
        return n1+n2
    if '.' in texto==True and '?' in texto==True:
        return n1+n3
    if '.' in texto==True and '...' in texto==True:
        return n1+n4
    if '.' in texto==True and '!' in texto==True and '?' in texto==True and '...' in texto==True:
        final=n1+n2+n3+n4
        return final