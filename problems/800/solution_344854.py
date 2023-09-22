# Questão 2
def total(lista=[], dic={}):
    c = 0.0
    
    for i in lista:
        c += dic[i]
    return round(c,2)