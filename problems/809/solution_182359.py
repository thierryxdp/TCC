# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista=[]
    for k in range(len(lista1)):
        lista +=lista1[k],lista2[k]
    return lista