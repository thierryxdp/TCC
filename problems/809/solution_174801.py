# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''Intercala as duas listas
    int,int-->int'''
    lista3 = [*sum(zip(lista1,lista2),())]
    return list(lista3)