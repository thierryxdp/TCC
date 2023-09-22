def faltante (lista):
    '''Funcao que, dada uma lista N-1, retorna o numero inteiro que está falatando.
    list->int'''
    
    i=0
    pecas=1
    list.sort(lista)
    L2=[]
    L3=[]
    while i != len(lista):
        if pecas == lista[i]:
            i=i+1
            pecas=pecas+1
        else:
            L2.append(pecas)
            i+=1
            pecas+=1
         
    if L2==L3:
        return lista[-1] + 1
        
    elif L2!=L3:
        return L2[0]