def repetidos(numeros):
    'dada uma lista retorne o numero de vezes que um elemento da lista é igual ao elemento anterior.list-->int'
    indice1=0
    indice2=indice1+1
    vezes=0
    while indice1<len(numeros) and indice2<len(numeros):
        if numeros[indice1]==numeros[indice2]:
            vezes=vezes+1
        indice1=i1+1
        indice2=i2+1
    return vezes