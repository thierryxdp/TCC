def repetidos(listnum):
   	'''Funçao que retorna o numero de vezes que um elemento da 
    lista e igual ao elemento anterior.
    listnum=list'''
    z=0
    h=0
    while z<len(listnum):
        if listnum[z]==listnum[z-1]:
            h=h+1
        z=z+1
    return h