# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que dado duas listas, gera uma terceira lista com
    os elementos intercalados  list, list -> list"""
    
    l1 = lista1
    l2 = lista2
    lista3 = [l1[0], l2[0], l1[1], l2[1], l1[2], l2[2]]
    
    return lista3