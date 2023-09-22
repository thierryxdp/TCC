def repetidos(lista):
    """
    Função que recebe uma lista de números
    e retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior.
    
    list ---> int
    """
    c=0
    for i in range(len(lista)-1):
        if lista[i]==lista[i+1]:
            c+=1
    return c