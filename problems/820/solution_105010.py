def posLetra(frase,letra,num):
    qnt_letra=0
    for x in frase:        
        if x==letra:
        qnt_letra+= 1
        if qnt_letra < num:
            return -1
        else:
            return qnt_letra