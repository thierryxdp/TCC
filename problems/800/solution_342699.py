def total(lista,dicio):
    soma=0
    indece=0
    for lista[indece] in dicio:
        soma=soma+dict.get(dicio,lista[indece])
    indece=indece+1
    return soma