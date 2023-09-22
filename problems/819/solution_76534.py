def filtroMultiplos(lista,n):
    """"função que, dada uma lista de números e um número n, retorna uma lista
    contendo os números que são divisíveis por n da lista dada como parâmetro.

    list, float -> list

    exemplos:
    filtromulti([1,2,3,4,5,6,7,8,9],3)==[3,6,9]
    filtromulti([1,2,3,4,5,6,7,8,9],2)==[2,4,6,8]"""
    i=0
    listaf=[]
    while i != len(lista):
        if lista[i]%n==0:
            listaf.append(lista[i])
        i=i+1
    return listaf