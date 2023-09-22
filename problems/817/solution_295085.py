def acima_da_media(lista):
    n = (sum(lista))/len(lista)
    def maiores(lista, n):
       list.append(lista, n)
       list.sort(lista)
       posicao = list.index(lista, n)
       l = lista[posicao+1:]
       return l