def filtraMultiplos(lista,n):
    '''
    '''    

    listaN=[]
    i=0
    divisao= lista[:]//n
    resto= n *divisao
    while i <len(lista):
        if divisao==resto:
            pos=i
            i=i+1
          
    return listaN