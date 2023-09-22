def filtraMultiplos(lista,num):
    '''função que retorn os multiplos do numero num; list,int->list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i] in [num*1,num*2,num*3,num*4,num*5,num*6,num*7,num*8,num*9]:
            multiplos=multiplos+[lista[1]]
        i=i+1
    return multiplos