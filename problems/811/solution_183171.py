def colchao(medidas:list,H:int,L:int)->bool:

    """ Função que retorna se é possível ou não passar o colchão por uma porta,
        Dados as medidas do colchão e a dimensão da porta


        Parameters:

        medidas: Lista com as dimensões do colchão, em ordem crescente (AxBxC)
        H: Altura da porta
        L: Largura da porta 

        Returns:

        Verifica se a dimensão intermediário do colchão é menor que a largura
        da porta e/ou a altura da porta.
        

    """

    if medidas[1] <= L:
    

        return True

    elif medidas[1]>=L and medidas[1]<=H:

        return True

    else:
        
        return False