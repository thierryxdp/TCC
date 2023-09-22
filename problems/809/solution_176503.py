# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    ''' Função que recebe duas listas "1 e 2" e intercala, retornando uma
    nova lista com os elementos das 2 listas'''
    #Casos de teste:
    ''' intercala([100,40,20],[45,53,10]) -> [100,45,40,53,20,10]
        intercala([550,55,2],[1500,430,20]) -> [550,1500,55,430,2,20]
        intercala([1,6,8],[10,5,2]) -> [1,10,6,5,8,2]'''
    a,b,c = lista1[0:3]
    x,y,z = lista2[0:3]
    lista3 = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return lista3