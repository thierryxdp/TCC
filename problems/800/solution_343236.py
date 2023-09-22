def total(lista,dic):
    soma=0
    for x in lista:
        soma= soma+dic[x]
    
    return round(soma,2)