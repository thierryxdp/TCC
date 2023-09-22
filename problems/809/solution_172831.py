# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    str(lista1)
    str(lista2)
    lista1=str.split(lista1)
    lista2=str.split(lista2)
    return lista1[0] + lista2[0] + lista1[1] + lista2[1] + lista1[2] + "," + lista2[2]