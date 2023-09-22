def total(lista,dicio):
    soma=0
    for i in lista:
        soma=soma+dicio[i]
    return round(soma,2)