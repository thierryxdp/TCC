def faltante(lista):
    """ A funçao faltante, dada uma lista com N − 1 inteiros numerados de 1 a N, descubre qual número inteiro deste intervalo está faltando.
        
        Parameters:
            lista = lista a ser averiguada

        Testes:
            faltante([1,2,3,4]) = 5
            faltante([4,2,3]) = 1
            faltante([1,2,6,3,4]) = 5
            
        Returns:
            número inteiro do intervalo inputadp que está faltando.
            list --> int
    """
    list.sort(lista)
    i=14
    fim = lista[-1]
    while i < fim:
        if i not in lista:
            return i
        i = i+1