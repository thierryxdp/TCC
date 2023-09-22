# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    for i in range(len(lista1)):
        lista3[2*i] = lista1[i]
        lista3[i*2+1] = lista2[i]
    return lista3