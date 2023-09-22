def intercala(lista1, lista2):
    '''Entrada: Lista1 (variável do tipo lista) e 
    Lista2 (variável do tipo lista)
       Saída: Lista3 (Nova lista formada intercalando os elementos 
       da lista1 e lista2'''
    soma1 = lista1 [0:1] + lista2 [0:1]
    soma2 = lista2 [1:2] + lista2 [1:2]
    soma3 = lista1 [2:] + lista2 [2:]
    return soma1+soma2+soma3