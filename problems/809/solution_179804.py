# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    a=lista1+lista2
    intercalado=a[0],a[3],a[1],a[4],a[2],a[5]
    return list(intercalado)