# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dadas duas listas lista1 e lista2 de tamanho 3 gera uma lista lista4 que é o intercalamento da lista1 e lista2 int,int -> int"""
    lista3 = lista1[0] + lista2[0] + lista1[1] + lista2[1] + lista1[2] + lista2[2]
    return lista3