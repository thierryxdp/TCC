def busca(area,matriz):
    '''Funcao que recebe uma matriz e faça uma busca por setor, ou seja, 
    dado um nome de um setor da empresa, a função retorna os dados de todos
    os funcionários daquele setor.
    str,list->list
    '''
    lista_final=[]
    for x in range(len(matriz)):
        if area== matriz[x][2]:
            lista=[]
            for y in range(len(matriz[0])):
                if y==2:
                    y+=1
                lista.append(matriz[x][y])
            lista_final.append(lista)
	return lista_final