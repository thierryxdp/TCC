def lista_unica(lista):
    result = []
    for item in lista:
        if (isinstance(item, (list, tuple))):
            result = lista.extend(item)
        else:
            result=result.append(item)
    return result
def media_matriz(matriz):
    matriz=lista_unica(matriz)
    mediaR = [i for i in matriz if i > 0]
    media = sum(matrizR) / len(matrizR)
    return media