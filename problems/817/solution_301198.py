def acima_da_media(notas):
    '''Função que retorna uma lista ordenada com as notas de
entrada que ficaram acima da média;
    lista -> lista;'''
    if len(notas)!=1:
    	n=(sum(notas)//len(notas))+1
    	list.append(notas,n)
    	list.sort(notas)
    	del notas[0:list.index(notas,n,0,-1)+1]
    	return notas
    else:
        return []