def intercala(lista1, lista2):
    '''
    função que soma da lista1 mais a lista2 
    gera a lista 3 intercalada
    entrada L1=[1,3,5] e saída L2=[2,4,6]
    '''
    lista1= [1,3,5]
    lista2= [2,4,6]
    lista3= [lista[1][0],lista[2][0],lista[1][1],lista[2][1],
             lista[1][2], lista[2][2]
             return lista3