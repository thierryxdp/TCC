def filtraMultiplos(numeros,n):
    """Recebe como entrada a lista números e o número n
    retorna apenas os números que são divisíveis por n
    list,int=>list"""
    acumulador=[]
    contador=0
    while contador < len(numeros):
        if numeros[contador] % n==0:
             list.append(acumulador,numeros[contador])
        contador = contador + 1
    return acumulador