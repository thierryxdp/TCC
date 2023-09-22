def busca(setor_empresa, matriz):
#Função que recebe uma matriz e faz uma busca por setor
#Retornando os dados de todos os funcionários daquele setor.    
    lista_matriz=[]
    
    for i in matriz:
        if i[2] == setor_empresa:
            i.remove(setor_empresa)
            lista_matriz.append(i)
            
    return lista_matriz