def repetidos(lista_numeros):
    """Função que recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    entrada:list
    saída: int"""
    i=1
    cont=0
    while i<len(lista_numeros):
        if lista_numeros[i]==lista_numeros[i-1]:
            cont=cont+1
            i=i+1
        else:
            i=i+1
    return cont