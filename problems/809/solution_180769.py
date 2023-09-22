# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ função que dadas duas listas L1 e L2 , 
    retorna uma nova lista , intercalando os 
    elementos das duas listas.
    assinatura: list,list--> list
    testes:
    intercala([1,3,5],[2,4,6]) == [1,2,3,4,5,6]
    intercala([10,20,30],[15,25,35]) == [10,15,20,25,30,35]
    intercala([0,4,8),[2,6,10])== [0,2,4,6,8,10]
    """
    lista3=[lista1[0],lista2[0],lista1[1],
            lista2[1],lista1[2],lista2[2]
            return lista3