# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(L1 : list, L2 : list)->list:
    """Dadas duas listas L1 e L2 de tamanho 3,retorna uma lista
    L3, que é formada intercalando os elementos de L1 e de L2,nessa ordem."""
       
    L3 = [L1[0],L2[0],L1[1],L2[1],L1[2],L2[2]]
    return L3