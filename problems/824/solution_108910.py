def uppCons(frase):
    lista=list(frase)
    for i in range(len(lista)):
        if lista[i] not in 'AEIOUaeiou':
            lista[i]= lista[i].upper
            separador=''
    return separador.join(lista)