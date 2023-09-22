# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1,lista2): #A função recebe duas listas
    lista3 = []
    for i in range(3):
        lista3.append(lista1[i]) #Adiciona o item i da lista 1 na lista3
        lista3.append(lista2[i]) #adiciona o item i da lista 2 na lista3
    return lista3 #Retorna a lista3