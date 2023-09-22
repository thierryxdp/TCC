def repetidos(lista):
    lista_numeros_unicos = []
    soma = 0
    for numero in range(0,len(lista)):
        if(lista[numero] == lista[numero-1]):
            soma += 1
        else:
            pass
    return soma