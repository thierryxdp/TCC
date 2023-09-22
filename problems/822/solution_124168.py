def repetidos(listnum):
   	'''Função que retorna o número de vezes que um elemento da 
    lista é igual ao elemento anterior.
    listnum=list'''
    p = 0
    h=0
    while x<len(listnum):
        if listnum[p]==listnum[p-1]:
            h=h+1
        p=p+1
    return h