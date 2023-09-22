def repetidos(lista):
    """"função que recebe como entrada uma lista de numeros, e retorna o numero
    de vezes que um elemento da lista é igual ao elemento anterior.

    list -> int

    exemplos:
    repetidos([1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7])==6
    repetidos([1,2,3,3,2,1,1,2,3,3,2])==3"""
    i=0
    acumulador=0
    while i!=len(lista):
        if lista[i]==lista[i-1]:
            acumulador=acumulador+1
        i=i+1
    return acumulador