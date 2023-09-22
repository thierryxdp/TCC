# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função
    faz e quais são os parâmetros de entrada e saída"""
    lista3 = []
    for a,b in zip(lista1, lista2):
        lista3.append(a)
        lista3.append(b)
    return lista3