def repetidos(listaNumeros):
    """ Recebe como entrada uma lista de números e retorna o número de vezes que um 
    elemento da lista é igual ao elemento anterior 
    list -> int """
    i, total = (0, 0)
    while i<len(listaNumeros):
        if i==len(listaNumeros)-1:
            return total
        if listaNumeros[i+1] == listaNumeros[i]:
            total+=1
        i+=1