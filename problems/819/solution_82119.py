def filtraMultiplos(lista_numeros,n):
    """Função que recebe como entrada uma lista de
    números 'lista_numeros' e um número 'n', e retorna
    outra lista contendo todos os elementos da lista
    original que forem divisiveis por 'n'."""
    i=0
    lista=[]
    while i<len(lista_numeros):
        if lista_numeros[i]%n ==0:
            lista = lista + [lista_numeros[i]]
        i= i+1
        
    return lista