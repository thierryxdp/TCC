def intercala(lista1, lista2):
   """função que dadas duas listas de tamanho 3 forma uma lista que intercala as listas 1 e 2"""
    lista1=['a','b','c']
    lista2=['x','y','z']
    var1= (lista1[0:1])+(lista2[0:1])
    var2= (lista1[1:2])+(lista2[1:2])
    var3= (lista1[2:])+(lista2[2:])
    lista3= var1+var2+var3
    return lista3