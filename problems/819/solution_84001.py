def filtraMultiplos(lista,numero):
    '''dsadasda'''
    l=list.sort(lista)
    i=0   
    multiplo=[]
    while lista[i]<l[-1]:
        if lista[i]%numero==0:
        	list.append(lista,lista[i])
    i=i+1
    return multiplo