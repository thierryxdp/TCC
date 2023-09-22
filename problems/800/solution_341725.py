def total(item,dicio):
    soma=0
    for el in item:
        if el in dicio:
        soma=soma+dicio[el]
    return round(soma,2)