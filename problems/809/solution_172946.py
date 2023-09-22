# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna uma lista intercalando os elementos das listas dadas;
    lista,lista->lista"""
    lista3 = lista1*2
    lista3[::2] = lista1
    lista3[1::2] = lista2 
    return lista3