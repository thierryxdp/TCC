def intercala(lista1, lista2):
    '''funcao que intercala os elementos de duas listas'''
    lista1 = [a,c,e]
    lista2 = [b,d,f]
    lista1[:1] + lista2[:1] + lista1[1:2] + lista2[1:2] + lista1[2:3] + lista2[2:3]