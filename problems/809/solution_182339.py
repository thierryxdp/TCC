# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """list,list -> list"""
    """recebe duas listas e intercala os elementos delas"""
    
    l1, l2 = lista1, lista2
    
    L = [l1[0]] + [l2[0]] + [l1[1]] + [l2[1]] + [l1[2]] + [l2[2]]
    
    return L