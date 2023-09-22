# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)+len(lista2)):
        lista3.append(lista1+lista2)
    return lista3