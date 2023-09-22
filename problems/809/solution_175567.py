def intercala(lista1, lista2):
    """Função que retorna uma lista L3, intercalando os elementos
    da lista1 e lista2
    lista1=list,lista2=list->list"""
    L1 = [lista1]
    L2 = [lista2]
    L3 = [L1[0],L2[0],L1[1],L2[1],L1[2],L2[2]]
    return L3