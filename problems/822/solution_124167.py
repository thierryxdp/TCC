def repetidos(listnum):
   	'''Função que retorna o número de vezes que um elemento da 
    lista é igual ao elemento anterior.
    listnum=list'''
    z = 0
    h=0
    while x<len(listnum):
        if listnum[z]==listnum[z-1]:
            h=h+1
        z=z+1
    return h