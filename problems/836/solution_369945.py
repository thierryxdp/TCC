def busca(setor_empresa, matriz):
    '''Função que recebe uma matriz contendo informações como nome, registro,
    setor e telefone de uma pessoa e recebe um setor específico ao qual ela retorna apenas
    as informações das pessoas que atuam nesse setor.
    tipo de entrada: str e list
    tipo de saída: list'''
    lista_matriz=[]
    
    for i in matriz:
        if i[2] == setor_empresa:
            i.remove(setor_empresa)
            lista_matriz.append(i)
                      
    return lista_matriz