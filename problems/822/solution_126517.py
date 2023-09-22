def repetidos(lista):
    """função que recebe uma lista com números e retorna a 
    quantidade de vezes que um elemento da lista é igual ao 
    elemento anterior.
    list -> <cont>"""
    i = 0
    cont = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            cont = cont + 1
        i = i + 1
    return cont