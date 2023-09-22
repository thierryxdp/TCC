def intercala(lista1, lista2):
    """função que recebe duas listas de tamanho 3 e gera uma
       nova lista que é formada pelos elementos das duas 
       primeiras intercalados.
       list, list -> list"""
    x1,x2,x3 = lista1
    y1,y2,y3 = lista2
    
    return lista1[0:1] + lista2[0:1] + lista1[1:2] + lista2[1:2] + lista1[2:3] + lista2[2:3] + lista1[3:3+1] + lista2[3:3+1]