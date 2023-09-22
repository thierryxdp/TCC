def lista_unica(lista):
    result = []
    for item in lista:
        if (isinstance(item, (list, tuple))):
            result = lista.extend(item)
        else:
            result.append(item)
    return result
def conta_numero(numero,matriz):
    matriz1=lista_unica(matriz)
    for i in matriz1:
    	repeticoes= matriz1.count(numero)
    return repeticoes