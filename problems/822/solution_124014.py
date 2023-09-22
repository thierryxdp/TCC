def repetidos (lista:list) ->int:
    """Função que recebe como entrada uma lsita de números e retorna o número de vezes que um
    elemento da lista é igual ao anterior."""
    numero = 0
    compara1= 0
    compara2= 1
    while compara2 <= len(lista):
        if lista[compara1] == lista [compara2]:
            numero = numero + 1
        compara1 = compara1 + 1
        compara2 = compara2 + 1
    return numero