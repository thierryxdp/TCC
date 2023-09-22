# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista3 = []
    for i in range(0,len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        return lista3