def intercala(lista1: list, lista2: list) -> list:
     """Dada duas listas de tamanho 3, gera uma terceira lista intercalando os itens da lista1 e lista2

       Parameters:
       lista1: primeira lista de 3 itens
       lista2: segunda lista de 3 itens

       Returns:
       Uma terceira lista intercalando os itens de lista1 e lista2
    """

    return lista1[0] + lista2[0] + lista1[1] + lista2[1] + lista1[2] + lista2[2]