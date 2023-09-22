# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    x = tuple(lista1)
    a,c,e = x
    y = tuple(lista2)
    b,d,f = y
    tupla = (a,b,c,d,e,f)
    return list(tupla)