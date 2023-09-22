def repetidos(lista: list) -> int:
    """Recebe uma lista de números e retorna o número de vezes que um elemento
       qualquer da lista é igual ao elemento imediatamente anterior à ele

       Parameters:
       lista: Lista composta por números a ser analisada

       Return:
       Dado o parâmetro "lista", retorna o número de vezes que um elemento
       qualquer da lista é igual ao elemento imediatamente anterior à ele

       Examples:
       repetidos([1, 2, 3, 4, 5]) == 0
       repetidos([1, 1, 2]) == 1
       repetidos([1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7]) == 6
    """

    ocorrencias = 0
    i = 0
    
    while i < len(lista):
        if  lista[i] == lista[i - 1]:
            ocorrencias = ocorrencias + 1
        i = i + 1

    return ocorrencias