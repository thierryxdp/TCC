def filtra_pares(t):
    lista=[]
    if type(t)==tuple and len(t)==4:
        for i in t:
            if type(i)!=int:
                lista=[]
                print('devem ser inteirs')
                break
                elif i%2==0:
                    lista.append(b)
                    return tuple(lista)