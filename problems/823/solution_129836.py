def faltante(lista):
    indice=0
    contador=1
    list.sort(lista)
    while indice != len(lista)-1:
        if contador==lista[indice]:
            indice+=1
            contador+=1
        else:
            break
    if contador==lista[-1]:
        return contador+1
    else:
        return contador