def posLetra(frase,letra,numero):
    contador = 0
    ocorrencia = 0
    lista = []
    while contador < len(frase):
        if frase[contador] == letra:
            ocorrencia = ocorrencia + 1
            list.append(lista, contador)
        contador = contador + 1
    return ocorrencia, lista