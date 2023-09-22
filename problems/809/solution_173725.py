# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    Função que intecala duas listas de tamanho 3, sendo que os elementos da primeira lista
    ocuparão os indices 0,2 e 4 e os elementos da segunda lista ocuparão os indices
    1,3,5.
    list, list --> list
    """
    a,b,c=lista1
    x,y,z=lista2
    lista3=[]
    lista3[0:2:4]=a,b,c
    lista3[1:3:5]=x,y,z
    return lista3