def maiores(lista):
    s=[n for n in lista if n(sum(lista))/len(lista))]
    list.sort(s)
    resturn s