# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dado como entrada duas listas como argumento, lista1 e lista2,
    de tamanho 3, retorna a lista l3 com o intercalamento das listas l1 e l2.
    Por exemplo, a lista1=[0,3,6] e lista2=[1,4,7] retornam a lista3=[0,1,3,4,6,7]
    lista(int)->lista(int)"""
    l1=lista1
    l2=lista2
    l3=[l1[0]]+[l2[0]] + [l1[1]]+ [l2[1]] + [l1[2]] + [l2[2]]
    return l3