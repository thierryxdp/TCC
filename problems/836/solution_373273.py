def busca(string, matriz):
    '''
Função que receba uma string e uma matriz que dado o nome de um setor da empresa, a funç̃ao retorna
uma lista com os dados de todos os funcionarios daquele setor.
  
str, list-->list
    '''
    lista=[]
   
    for string in matriz:
        if matriz[i][j]==string:
            lista+=matriz[i][j]
            return lista
            
        else:
            return []