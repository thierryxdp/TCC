def intercala(lista1,lista2):
    """Dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que é formada intercalando os elementos de L1 e L2
    list, list - list"""
    Lista=[]
    if len(lista1)==3 and len(lista2)==3:
        return Lista+(lista1[:1])+(lista2[:1])+(lista1[1:2])+(lista2[1:2])+(lista1[2:3])+(lista2[2:3])