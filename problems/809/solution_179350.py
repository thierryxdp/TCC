# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''lista1 -> list[int,int,int]
       lista2 -> list[int,int,int] '''
    [a,b,c] = lista1
    [d,e,f] = lista2
    L3 = [lista1[0]]+[lista1[1]]+[lista1[2]]+[lista2[0]]+[lista2[1]]+[lista2[2]]
    return L3