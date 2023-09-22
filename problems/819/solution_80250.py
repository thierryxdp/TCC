def filtraMultiplos (lista_numeros,num):
    """Função que recebe uma lista de números e um número e retorna uma lista contendo todos os elementos da lista original que forem divisíves por esse número
    entrada: list, int
    saída: list"""
    i=0
    lista_final=[]
    while i<len(lista_numeros):
        if lista_numeros[i]%num == 0:
            lista_final=lista_final+lista_numeros[i]
            i=i+1
    return lista_final