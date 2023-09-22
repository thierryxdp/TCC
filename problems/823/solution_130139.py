def faltante(lista):
    """ A funçao faltante, dada uma lista com N − 1 inteiros numerados de 1 a N, descubre qual número inteiro deste intervalo está faltando.
        
        Parameters:
            lista = lista a ser averiguada

        Testes:
            faltante(10) = 3628800
            faltante(5) = 120
            faltante(3) = 6
            
        Returns:
            número inteiro do intervalo inputadp que está faltando.
            list --> int
    """
    list.sort(lista)
    i=1
    fim = lista[-1]+1
    while i <= fim:
        if i not in lista:
            return i
        i = i+1