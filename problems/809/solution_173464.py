def intercala(lista1, lista2):
    """Função que recebe como entrada duas listas (L1 e L2) de tamanho 3, e gera 
    uma lista L3 que intercala os elementos de L1 e L2."""
    """list,list-->list"""
    resultado=[]
    resultado.append(lista1[0])
    resultado.append(lista2[0])
    resultado.append(lista1[1])
    resultado.append(lista2[1])
    resultado.append(lista1[2])
    resultado.append(lista2[2])
    return resultado