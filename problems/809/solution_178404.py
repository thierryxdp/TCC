# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
"""Funcao que dada duas listas,retorna a concatenacao das listas; list,list = list.""" 
    lista1=[1,3,5]
    lista2=[2,4,6]
    lista3=lista1+lista2
    lista3 [::2]=lista1
    lista3[1::2]=lista2
    return lista3