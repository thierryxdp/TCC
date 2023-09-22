def busca(nomesetor,matriz):
    '''teste'''
    listacontato=[]
    listasetor=[]
    pos=0
    for i in matriz:
        posn=0
        for j in matriz[pos]:
            if nomesetor==matriz[pos][posn]:
                lista=lista+matriz[pos]
                list.remove(lista,numsetor)
                listasetor=listasetor+lista
            posn=posn+1
		pos=pos+1
			return listasetor,pos,posn