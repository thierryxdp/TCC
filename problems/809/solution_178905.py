# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    Dadas duas listas (L1 e L2) com três elementos cada, esta função 
    reorna uma terceira lista com os elementos intercalados 
    das duas listas originais L1 e L2
    """
    L1=lista1
    L2=lista2
    L3=[1,1,1,1,1,1]
    L3[0]= L1[0]
    L3[1]= L2[0]
    L3[2]= L1[1]
    L3[3]= L2[1]
    L3[4]= L1[2]
    L3[5]= L2[2]
    return L3