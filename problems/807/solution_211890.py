#Questão 2
def conta_frases(texto):
    """função que conta o número de frases
que aparecem no texto"""
    x = str.count(texto,'.') 
    y = str.count(texto,'!')
    z = str.count(texto,'?')
    w = str.count(texto,'...') - str.count(texto,'...')*3
    
    return x+y+z+w