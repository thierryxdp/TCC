def repetidos(lista):
    rep = 0
    for n in range(len(lista)):
        for m in range(len(lista)):
            for o in range(len(lista)):
                if(lista[n]==lista[n+1]):
                    rep = +1
                elif(lista[m]==lista[m+1]):
                    rep = +1
                elif(lista[o]==lista[o+1]): 
                    rep = +1
                else:
                    return rep+1