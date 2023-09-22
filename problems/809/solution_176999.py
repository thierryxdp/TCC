# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dada duas listas de tamanho 3 nos parâmetros, retorna outra lista com elementos das listas anteriores intercalados; list, list -> list"""
    L3= lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:] + lista2[2:]
    return L3