def busca(string, matriz):
    '''
Função que receba uma string e uma matriz que dado o nome de um setor da empresa, a funç̃ao retorna
uma lista com os dados de todos os funcionarios daquele setor.
  
str, list-->list
    '''
    lista=[]
   
    for i in matriz:
        if matrz[i]==string:
            lista=[ matriz[i]]
            lista+=[matriz[i]]
            return lista
            
        else:
            return []