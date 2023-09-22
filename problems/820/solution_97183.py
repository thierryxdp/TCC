def posLetra(frase,letra,n):
    ''';
    str,str,int->'''
    frasi=list(frase)
    tam=len(frasi)
    indy=[]
    qtd=str.count(frase,letra)
    i=0
    if qtd<=n:
    	while i<tam:
        	if frasi[i]==letra:
                list.append(indy,frasi[i])
            i=i+1
        indy[n]='tx'
        str.replace(frase,letra,'tx')
        return list.index(frasi,'tx')
    else:
        return -1