# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que recebe duas listas e retorna uma nova lista com os elementos da primeira e da segunda lista intercalados; list,list->list"""
    e1=lista1[0]
    e2=lista2[0]
    e3=lista1[1]
    e4=lista2[1]
    e5=lista1[2]
    e6=lista2[2]
    lista3=[e1]+[e2]+[e3]+[e4]+[e5]+[e6]
    return lista3