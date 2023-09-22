# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """essa funcao, dadas duas listas L1, L2 como parametro de entrada, retorna
	 uma terceira lista formada pelos elementos de L1 e L2 intercalados.
	list, list -> list"""
    
    L3 = lista1 + lista2
    
    L3[0] = lista1[0]
    L3[1] = lista2[0]
    L3[2] = lista1[1]
    L3[3] = lista2[1]
    L3[4] = lista1[2]
    L3[5] = lista2[2]
    
    return L3