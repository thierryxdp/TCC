def repetidos(lista):
    proximo=0
    total=()
    while proximo<len(lista):
        if lista[proximo]==lista[proximo-1]:
            list.append(total,1)
        proximo = proximo +1 
    return sum(total)