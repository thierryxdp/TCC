def filtraMultiplos(lista,n):
    
    divisiveis=[]
    while len(lista)!=0:
        a=lista[-1]
        if a%n==0:
           list.append(divisiveis,a)
           del lista[-1]
            a=lista[-1]
        else:
            del lista[-1]
            a=lista[-1]

        return divisiveis