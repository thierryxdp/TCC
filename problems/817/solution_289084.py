def acima_da_media(lista):
    média =sum(lista)/len(lista)
    list.append(lista, média)
    list.sort(lista)
    posição_da_média =list.index(lista, média)
    maiores_que_média =lista[(posição_da_média+1):]
    return maiores_que_média
##([10,30,40,50]);([30,40,40,40])