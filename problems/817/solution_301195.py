def acima_da_media(notas):
    '''Função que retorna uma lista ordenada com as notas de
entrada que ficaram acima da média;
    lista -> lista;'''
    n=(sum(notas)//len(notas))+1
    #n=5
    list.append(notas,n)
    list.sort(notas)
    del notas[0:list.index(notas,n,0,-1)+1]
    if len(notas)==0
    	return []
    else:
        return notas