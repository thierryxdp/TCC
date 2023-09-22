def repetidos(lista):
    '''recebe como entrada uma lista de numeros e retorna
    quantas vezes um elemento é igual ao anterior
    list->int'''
    cont=0
    acum=0
    while cont<len(lista)-1:
        if lista[cont]==lista[cont+1]:
            acum=acum +1
        cont=cont+1
    return acum