def repetidos(numeros):
    'dada uma lista retorne o numero de vezes que um elemento da lista é igual ao elemento anterior.list-->int'
    i1=0
    i2=i1+1
    vezes=0
    while lista[i1]==lista[i2]:
        vezes=vezes+1
        i1=i1+1
        i2=i2+1
    return vezes