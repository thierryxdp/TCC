def filtraMultiplos(lista,n):
    '''
    '''    

    listaN=[]
    i=0
    divisao= lista[:]//n
    resto= n *divisao
    a=divisao==resto
    while i <len(lista):
        if lista[i]==a:
            pos=i
            i=i+1
          
    return listaN