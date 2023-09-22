# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que intercala as listas que foram dadas. 
    Ex:lista1=[1,3,5],lista2=[2,4,6] -> [1, 2, 3, 4, 5, 6]
    list[int,int,int],list[int,int,int]"""
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]