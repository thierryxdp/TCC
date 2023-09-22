def acima_da_media(lista):
    lista= sorted(lista)
    media= sum(lista)//(len(lista)-1)
    resultado = []
    for i in range(len(lista)):
        if lista[i]>=media:
            resultado.append(lista[i])

    return resultado