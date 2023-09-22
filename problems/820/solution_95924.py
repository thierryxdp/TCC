def posLetra(frase, letra, n):

    lista = list(frase)
    i = 0
    ocorrencia = 0

    while i <= (len(lista) - 1) and ocorrencia <= n:
        if lista[i] == letra:
            ocorrencia = ocorrencia + 1

        i = i + 1
        
    return i