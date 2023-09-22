def intercala(lista1, lista2):
    """Intercala os itens de duas listas de tamanho 3.
       list,list->list
       
       Parameters:
       lista1: A primeira lista.
       lista2: A segunda lista.
       
       Returns:
       Uma terceira lista de tamanho 6 que foi formada intercalando a lista1 e a lista2"""
    
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]