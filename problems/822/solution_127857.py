def repetidos(lista):
    """
    Essa função, ao ser dado uma lista como argumento ela ira retornar a quantidade de vezes que um
    elemento da lista é igual ao seu anterios
    list->int
    """
    
    contador = 1
    repetidos = 0
    
    while contador<= len(lista) - 1:
        
        if lista[contador] == lista[contador-1]:
            repetidos = repetidos + 1
        contador = contador + 1
    return repetidos