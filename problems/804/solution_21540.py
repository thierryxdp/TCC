def filtra_pares(t):
    (a,b,c,d)=t
    lista = []
    for a in t :
        if a % 2 == 0:
            lista.append(a)
            else:
                if b % 2 == 0:
                    lista.append(b)
                    else:
                        if c % 2 == 0:
                            lista.append(c)
                            else:
                                if a % 2 == 0:
                                    lista.append(a)
                                    return tuple(lista)
                            
                
            
         
            return tuple(lista)