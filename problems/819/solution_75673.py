def filtraMultiplos(lista,n):
    a=lista[-1]
    divisiveis=[]
    while len(lista)!=0:
        if a%n==0:
           list.append(divisiveis,a)
           del lista[-1]
        else:
            del lista[-1]

        return divisiveis