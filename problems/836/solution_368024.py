def busca(nomesetor,matriz):
    '''teste'''
    listacontato= []
    listasetor= []
    pos=0
    for i in matriz:
        posn=0
        for j in matriz[pos]:
            if nomesetor==matriz[pos][posn]:
                listacontato=listacontato+matriz[pos]
                list.remove(listacontato,nomesetor)
                listasetor=listasetor+listacontato
        			posn=posn+1
			pos=pos+1
	return listasetor,pos,posn