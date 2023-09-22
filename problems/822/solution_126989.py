def repetidos(lista):
    'Retorna o número de vezes que um elemento da lista é igual ao anteiror'
    'lista -> int'
    contador=0
    i=1
    while i<len(lista):
        if lista[i]==lista[i-1]:
            contador=contador+1
        i=i+1
    return contador