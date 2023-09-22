def repetidos(lista):
    """
    Essa função recebe uma lista de números e retorna 
    o número de vezes que um elemento da lista é igual ao 
    seu anterior;
    list -> int
    """
    frente = 1
    str1 = ''
    n_repetido = 0
    for x in lista:
        str1 += str(x)
    
    for i in range(0, len(str1)):
        if str1[i] == str1[frente]:
            n_repetido +=1
            continue
        frente += 1
    return n_repetido