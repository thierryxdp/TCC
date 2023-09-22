def intercala(lista1, lista2):
    '''a função intercala os elementos de duas listas de 
    tamanho (len) = 3. Pressupões-se que será adc duas 
    listas com 3 elementos cada
    lista -> lista'''
    
    lista1 = [lista1[0], lista1[1], lista1[2]]
    lista2 = [lista2[0], lista2[1], lista2[2]]
    
    L3= [lista1[0], lista2[0], lista1[1], lista2[1],
         lista1[2], lista2[2]]
    
    return L3