#---------------------EXERCICIO 4---------------------
def repetidos(lista_numeros):
    '''retorna quantos elementos repetidos há em uma lista
       list -> int'''

    list.sort(lista_numeros)
    i = 0
    j = 0
    x = []
    y=[]
    repeticoes = 0

    while i<len(lista_numeros):
        if lista_numeros[i] not in x:
            x.append(lista_numeros[i])
        else:
            if lista_numeros[i] not in y:
                y.append(lista_numeros[i])
        i += 1
    return len(y)