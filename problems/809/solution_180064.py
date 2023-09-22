# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    listan = lista1+lista2
    lista1 = listan[0:-1:3]
    lista2 = listan[1:-1:3]
    lista3 = listan[2:-1:3]
    return lista1+lista2+lista3