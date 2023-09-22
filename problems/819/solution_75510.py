def filtraMultiplos(lista, n):
    """Função que recebe uma lista de numeros e  numero n,
    retornando uma lista contendo os numeros divisiveis por n
    entrada: lista, int
    retorno: lista"""
    lista_saida== list[}
    i= 0
    while i< len(lista):
        if lista[i] % n ==0:
            lista_saida.append(lista[i])        
        i= i+1
    return lista_saida