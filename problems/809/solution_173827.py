# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    x = lista1, lista2
    a = str.split(",",x)
    b = sorted(a)
    return str.join(b,x)