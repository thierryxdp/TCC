# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que retorna a lista 1 intercalada com a lista 2, formando assim uma lista 3
    entrada: list, list
    saida: list"""
    return lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:3] + lista2[2:3]