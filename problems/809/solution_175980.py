# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    """
    c = lista1*2
    c[1::2] = lista2
    c[::2] = lista1
    
    return c