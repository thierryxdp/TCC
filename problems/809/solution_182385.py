def intercala(lista1,lista2):
    """Função que intercala os elementos das listas de tamanho 3, formando outra lista como resultado"""
    l3= []
    l3[0:1]=[lista1[0]]
    l3[1:2]=[lista2[0]]
    l3[2:3]=[lista1[1]]
    l3[3:4]=[lista2[1]]
    l3[4:5]=[lista1[2]]
    l3[5:6]=[lista2[2]]
    return l3