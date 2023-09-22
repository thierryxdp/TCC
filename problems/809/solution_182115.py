# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """recebe duas listas de tamanho 3 e gera uma nova lista intercalando os elementos das listas de entrada
    list + list -> list"""
    l3 = lista1 + lista2
    l3[::2] = lista1
    l3[1::2] = lista2
    return l3