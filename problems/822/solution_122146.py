def repetidos(lista):
    """ A funçao repetidos recebe como entrada uma lista de números, e retorna o número de vezes que um elemento da lista é igual ao elemento anterior. 
        
        Parameters:
            lista = lista a ser verificada sobre as codicoes citadas

        Testes:
            repetidos([1,4,3,3,2,3,3,3,3,5,4,6,6,7,6,8,8,7]) = 6
            repetidos([1,1,1,1,1,1,1,1,2,3,4,5]) = 7
            repetidos([2,3,4,5,6,7,8]) = 0
            
        Returns:
            número de vezes que um elemento da lista é igual ao elemento anterior.
            list --> int
    """
    i = 0
    resultado = 0
    while i<len(lista)-1:
        if lista[i] == lista[i+1]:
            resultado = resultado + 1
        i=i+1

    return resultado