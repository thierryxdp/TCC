# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista_nova=lista1[0:0]+lista2[0:0]+lista1[0:1]+lista2[0:1]+lista1[-1:-2]+lista2[-1:-2]
    return lista_nova