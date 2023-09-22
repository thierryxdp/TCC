# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    i = 0
    lista3 = []
    while i < 3:
        lista3.append(lista1[i])
        lista3.append(lista2[i])
        i += 1
    return lista3