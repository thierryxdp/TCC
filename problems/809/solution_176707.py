# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2,lista3=lista1+lista2):
    '''Intercala os valores de duas listas em ordem'''
    return lista3[1::3],lista3[2::3],lista3[3::3]