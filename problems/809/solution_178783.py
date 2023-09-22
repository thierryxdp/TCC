# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    lista1.insert(1, lista2[0])
    lista1.insert(3, lista2[1])
    lista1.insert(5, lista2[2])
    return lista1