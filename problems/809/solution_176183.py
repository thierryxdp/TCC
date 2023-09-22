# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Funcao que gera uma terceira lista pela intercalacao dos parametros
    (lista1) e (lista2).
    list, list -> list"""
    ListaA = lista1[0] + lista2[0] + lista1[1] + lista2[1]
    ListaB = lista1[2] + lista2[2]
    lista3 = ListaA + ListaB
    return lista3