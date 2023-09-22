# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
'''retorna a uniao de duas listas, intercalando seus valores de maneira crescente'''
def intercala(lista1, lista2):
    listaA = lista1[0:1] + lista2[0:1]
    listaB = listaA[:] + lista1[1:2] + lista2[1:2]
    listaC = listaB[:] + lista1[2:3] + lista2[2:3]
    listaE = listaC[:] + lista1[3:] + lista2[3:]
    return listaE