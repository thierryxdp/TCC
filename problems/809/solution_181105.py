# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """funcao que intercala duas listas de tamanho 3 em uma;
    list, list -> list"""
    return lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1 [2:] + lista2[2:]