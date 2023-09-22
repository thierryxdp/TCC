# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3
    que  ́e formada intercalando os elementos de L1 e L2.
    lista,lista -> lista
    """
    return list(str.join(str(lista2[0]),str(lista1[0]))+str.join(str(lista1[0]),str(lista2[0]))
            +str.join(str(lista2[1]),str(lista1[1]))+str.join(str(lista1[1]),str(lista2[1]))\
            +str.join(str(lista2[2]),str(lista1[2]))+str.join(str(lista1[2]),str(lista2[2])))