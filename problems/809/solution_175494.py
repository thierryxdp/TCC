def intercala(lista1, lista2):
    """Funcao que dadas duas listas de tamanho 3, no caso, 
    lista1 e lista2, gera uma terceira lista, no caso, a 
    lista3, que e formada intercalando os elementos da 
    lista1 e lista2. Exemplo: lista1=[1,3,5] e lista2=[2,4,6]
    gera lista3=[1,2,3,4,5,6];
    lista,lista->lista"""
    return [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],
            lista2[2]]