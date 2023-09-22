def filtraMultiplos(lista,n):
    
    
    resposta = list()
    num_elementos = len(numeros)
    indice = 0

    while (indice < num_elementos):
        if (numeros[indice] % n == 0):
            list.append(resposta, lista[indice])
        indice += 1

    return list(resposta)