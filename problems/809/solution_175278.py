# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    for a,b in zip(lista1,lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada
lista1 = [1,2,3]
lista2 = [4,5,6]
listalntercalada = intercala(lista1, lista2)