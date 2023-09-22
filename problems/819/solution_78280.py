def filtraMultiplos(lista,n):
    """Retorna uma lista com todos elementos da lista original que forem
    divisíveis por n; list,int->list"""
    cont=0
    acumulador=[]
    while cont<len(lista):
        if lista[cont]%n==0:
            list.append(acumulador,lista[cont])
        cont=cont+1
    return acumulador