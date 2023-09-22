def acima_da_media(lista):
    list.append(lista, sum(lista)/len(lista))
    list.sort(lista)
   
    return lista[(list.index(lista, int(sum(lista)/len(lista)))+1):]
##([10,30,40,50]);([30,40,40,40])