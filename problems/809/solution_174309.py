# dadas duas listas de tamanho 3 ele gera uma L3 que é formada intercalados os elementos das listas
# Lista1 e Lista2
def intercala(Lista1, Lista2):
    """Recebe as duas listas e intercala elas entre si"""
    Lista3 = Lista1+Lista2
    return Lista3[1]+Lista3[3]+Lista3[2]+Lista3[4]+Lista3[6]+Lista3[5]