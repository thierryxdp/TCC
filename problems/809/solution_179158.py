# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dadas duas listas L1 E L2 de tamanho 3,
    gera uma lista L3 que é formada intercalando os elemenos
    list, list -> list"""
    
    L3 = lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:] + lista2[2:]
    
    return L3