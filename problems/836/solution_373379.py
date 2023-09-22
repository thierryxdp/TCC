def busca(string, matriz):
    '''
Função que receba uma string e uma matriz que dado o nome de um setor da empresa, a funç̃ao retorna
uma lista com os dados de todos os funcionarios daquele setor.
  
str, list-->list
    '''
    lista=[]
    for i in range(len(matriz)):
        linha=0
        for j in range(len(matriz[0])):
            if string==matriz[i][0]:
                linha.append([matriz[i]])
                lista.append(linha)
                del matriz[i][2]
                return lista