# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dada uma lista1 com 3 elementos e uma lista2 com
    3 elementos teremos uma nova lista com
    [linsta1[0],lista2[0]lista1[1],lista2[1],lista1[2],lista2[2]]"""
    a=lista1[0]
    b=lista1[1]
    c=lista1[2]
    x=lista2[0]
    y=lista2[1]
    z=lista2[2]
    return [a]+[x]+[b]+[y]+[c]+[z]