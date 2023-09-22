# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dada duas listas retorna uma terceira lista intercalando l1 e l2.
    parametros lista->lista"""
    L1 = [lista1]
    L2 = [lista2]
    L3 = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return L3