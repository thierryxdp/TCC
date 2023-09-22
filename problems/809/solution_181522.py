# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que  ́e formada
    intercalando os elementos de L1 e L2;
    Assinatura:list,list-->list
    testes:
    intercala([6,2,7],[5,9,1])==[6, 5, 2, 9, 7, 1]
    intercala([4,2,3],[6,2,5])==[4, 6, 2, 2, 3, 5]
    intercala([7,6,4],[5,2,0])==[7, 5, 6, 2, 4, 0]
    """
    listas= [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return listas