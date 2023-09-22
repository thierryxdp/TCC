def filtraMultiplos(lista,n):
    '''Função que recebe como entrada uma lista de números e um número n e retorna uma lista com todos os elementos da lista original que são divisiveis por n; list,float->list'''
    listanova=[]
    contador=0
    while contador<len(lista):
        if lista[contador]%n==0:
            list.append(listanova,lista[contador])
        contador = contador + 1
    return listanova