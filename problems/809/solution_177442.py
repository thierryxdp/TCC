# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """A função intercala duas listas de entrada e dá uma terceira lista de saída"""
    a = [lista1[0]] + [lista2[0]]
    b = [lista1[1]] + [lista2[1]]
    c = [lista1[2]] + [lista2[2]]
    lista3 = a + b + c
    
    return lista3