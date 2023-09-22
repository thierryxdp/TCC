def busca(M,s):
    """Os dados dos funcionarios de uma empresa sao 
    armazenados em uma matriz na qual cada linha tem quatro
    entradas,representando as informacoes referentes a nome,
    registro, setor e telefone de um funcionario, nesta 
    ordem. O numero de linhas depende da quantidade de 
    funcionarios. Todas as entradas da matriz estao em
    formato string. Esta funcao recebe como entrada uma 
    matriz M e faz uma busca por setor s, ou seja, dado um
    nome de um setor da empresa, a funcao retorna os dados
    de todos os funcionarios daquele setor em uma lista. Se 
    nenhum registro for encontrado, a funcao retorna uma 
    lista vazia; 
    lista,str->lista"""
    
    L=[]
    
    for i in range(len(M)):
        if M[i][2]==s:
            L=L+[[M[i][0],M[i][1],M[i][3]]]
                
    return L