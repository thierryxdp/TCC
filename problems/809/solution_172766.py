def intercala(lista1, lista2):
    """Esta é a função que dada duas listas de tamanho 3, retorna uma outra lista intercalando os elementos das duas originais, lista -> lista"""
    a= lista1[0]
    b= lista1[1]
    c= lista1[2]
    d= lista2[0]
    e= lista2[1]
    f= lista2[2]
    lista3 = [a]+[d]+[b]+[e]+[c]+[f]
    return lista3