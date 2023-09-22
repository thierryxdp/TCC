def busca(setor,dados):
    '''Realiza uma busca e retorna os dados de todos os
       funcionários de determinado setor numa empresa;
       str, list -> list'''
    
    dados_buscados = []
    
    for linhas in dados:
        
        funcionario = []
        
        if linhas[2] == setor:
            
            funcionario.append(linhas[0])
            funcionario.append(linhas[1])
            funcionario.append(linhas[3])
            dados_buscados.append(funcionario)
            
    return dados_buscados