'''função que calcula a quantidade de frases em umm texto, separando essas frases em suas respectivas pontuações
str->int'''

def conta_frases(texto):
    
    ponto final=str.count(texto,'.')
    exclamação=str.count(texto,'!')
    interrogação=str.count(texto,'?')
    tres pontos=str.count(texto,'...')
   
    return ponto-3*tres pontos+tres pontos+ exclamação+ interrogação