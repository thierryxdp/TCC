def total (lista,d):
    """ Retorna o somatório dos valores do dicioonário que tem as suas respectivas 
    chaves na lista 
    list, dict--> float"""
    Bianca = 0
    for i in range (len(lista)):
        if lista [i] in list (dict.keys(d)):
            Bianca+= dict.get(d,lista[i])
return round(Bianca,2)