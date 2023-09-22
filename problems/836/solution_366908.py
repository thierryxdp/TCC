def busca(setor,matriz):
    """dado um nome de um setor e uma matriz, a função retorna os dados
    dos funcionários daquele setor.
    str, list-->list
    
    Parâmetros
    indice1: índice do primeiro while
    indice2: índice do segundo while
    indice3: índice do terceiro while
    setor: setor que será buscado na matriz
    matriz: matriz com os dados dos funcionários
    """
    lista=[]
    indice1=0
    while indice1<len(matriz):
        indice2=0
        while indice2<len(matriz[0]):
            if matriz[indice1][indice2]==setor:
                list.append(lista,matriz[indice1])
            indice2=indice2+1
        indice1=indice1+1
    if lista!=[]:
        indice3=0
        while indice3<len(lista):
            list.pop(lista[indice3],2)
            indice3=indice3+1
        return lista
    else:
    	return []