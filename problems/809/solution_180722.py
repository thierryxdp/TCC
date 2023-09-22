# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    resp1= lista1[::2]
    resp2= lista2[::2]
    resp01=lista1[1::2]
    resp02=lista2[1::2]
    return resp1, resp01, resp01, resp02