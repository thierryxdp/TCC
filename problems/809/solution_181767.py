# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Pega duas listas e intercalas seus elementos"""
    L3= lista1 + lista2
    L3[::2]= lista1
    L3[1::2]= lista2
    return L3