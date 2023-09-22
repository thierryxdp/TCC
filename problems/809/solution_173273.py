# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """retorna uma funcao que cria uma nova lista com
    os valores intercalados de duas listas ja existentes
    sendo as listas de entrada composta por apenas tres numeros
    e a lista nova criada composta por seis numeros
    list,list->list"""
    [x,y,z]=lista1
    [a,b,c]=lista2
    lista3=[lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]
    return lista3