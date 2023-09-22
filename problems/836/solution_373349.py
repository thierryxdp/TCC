def busca(string, matriz):
    '''
Função que receba uma string e uma matriz que dado o nome de um setor da empresa, a funç̃ao retorna
uma lista com os dados de todos os funcionarios daquele setor.
  
str, list-->list
    '''
    lista=[]
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[0])):
            if matriz[i]==[string]:
                linha.append(matriz[i])
                lista.append(linha)
                return lista
            
            else:
                return []