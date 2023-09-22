# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """funcao q recebe duas listas e as intercanla numa terceira
    lista"""
    a=lista1[0],lista2[0],lista1[1]
    b=lista2[1],lista1[2],lista2[2]
    return list(a) + list(b)