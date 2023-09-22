# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que, dado duas lista L1 e L2  de tamanho 3, gera uma terceira lista L3
       que é formada pela intercalação dos elementos das listas L1 e L2.
       int, int -> int"""
    A = lista1[0] , lista2[0] ,lista1[1]
    B = lista2[1] , lista1[2] , lista2[2]
    return lista(A) + lista (B)