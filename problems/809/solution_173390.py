# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função calcula a intercala(lista1,lista2) que dadas duas listas L1 e L2 de tamanho 3, gera uma lista L3 que e formada intercalando os elementos de L1 e L2: list->list"""
    elemento0L1=lista1[0]
    elemento1L1=lista1[1]
    elemento2L1=lista1[2]
    elemento0L2=lista2[0]
    elemento1L2=lista2[1]
    elemento2L2=lista2[2]
    return [elemento0L1,elemento0L2,elemento1L1,elemento1L2,elemento2L1,elemento2L2]