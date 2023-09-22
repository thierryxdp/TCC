def uppCons(frase):
    lista=list(frase)
    for i in range(len(lista)):
        if lista[i] not in 'AEIOUaeiouãóúíé':
            lista[i]= lista[i].upper()
            separador=''
    return separador.join(lista)