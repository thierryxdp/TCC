def maiores(lista, n):
	teto=n
   
    for x in lista:
        listanova=[]
        if x>teto:
            listanova = listanova.append(x)
        else:
            return listanova.sort()