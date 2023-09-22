def repetidos(lista):
    """Função que retorna a quantidade de vezes que um elemento da lista é
    igual ao elemento anterior. list -> int"""
    i = 0
    i2 = 1
    cont = 0
    while i2 < len(lista):
        if lista[i] == lista[i2]:
            cont = cont + 1
        i = i + 1
        i2 = i2 + 1
    
    return cont