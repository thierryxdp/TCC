def busca(string, matriz):
    '''
Função que receba uma string e uma matriz que dado o nome de um setor da empresa, a funç̃ao retorna
uma lista com os dados de todos os funcionarios daquele setor.
  
str, list-->list
    '''
    lista=[]
    
    for i in range(len(matriz)):
        qtd=0
        for j in range(len(matriz[0])):
            qtd+=matriz[i][j]
        list.append(lista,qtd)

    return lista
            
    if string not in matriz :
        return []