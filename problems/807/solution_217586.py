'''função que calcula a quantidade de frases em umm texto, separando essas frases em suas respectivas pontuações
str->int'''

def conta_frases(texto):
    
    ponto=str.count(texto,'.')
    exclamacao=str.count(texto,'!')
    interrogacao=str.count(texto,'?')
    trespontos=str.count(texto,'...')
   
    return ponto-3*trespontos+trespontos+ exclamacao+ interrogacao