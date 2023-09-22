def posLetra(string,letra,ocorrencia):
    string = list(string)
    ocorrencias = []
    i = 0 
    while i < len(string):
        if string[i] == letra:
            ocorrencias.append(i)
            i += 1
        i += 1
    if ocorrencia <= (len(ocorrencias)):
        ocorrencia = ocorrencia-1
        ocorrencias[ocorrencia]
        return ocorrencias[ocorrencia]
    else:
        return -1

    
# repetidos
def repetidos(lista):
    """Essa função recebe uma lista de numeros e conta quantas vezes numeros consecutivos se repetem
    list ->int"""
    contador = 0
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            contador += 1
    return contador