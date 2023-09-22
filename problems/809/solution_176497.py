# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    ''' Função que recebe duas listas "1 e 2" e intercala, retornando uma
    nova lista com os elementos de em ordem crescente'''
    ''' função "sorted" ordena de forma crescente os elementos intercalados
    das listas 1 e 2'''
    #Casos de teste:
    ''' intercala([100,40,20],[45,53,10]) -> [10,20,40,45,53,100]
        intercala([550,55,2],[1500,430,20]) -> [2,20,55,430,550,1500]
        intercala([1,6,8],[10,5,2]) -> [1,2,5,6,8,10]'''
    a,b,c = lista1[0:3]
    x,y,z = lista2[0:3]
    lista3 = lista1 + lista2
    return sorted(lista3)