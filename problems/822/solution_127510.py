def repetidos(lista):
    '''Função que pega lista de entrada, e retorna a quantidade de elementos iguais aos anteriores
    list,list→int''''
    indice=0
    soma= 0
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
        	soma+=1
        indice+=1
    return soma