# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ Insira as duas listas para que a função intercale elas e retorna uma terceira lista"""
    lista3=[]
    for i in range (0,len(lista1)):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3