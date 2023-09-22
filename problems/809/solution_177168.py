# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    listaA = lista1[0:1] + lista2[0:1]
    listaB = listaA[:] + lista1[1:2] + lista2[1:2]
    listaC = listaB[:] + lista1[2:3] + lista2[2:3]
    listaE = listaC[:] + lista1[3:] + lista2[3:]
    return listaE