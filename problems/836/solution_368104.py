def busca(setor, matriz):
    '''Função que recebe string e lista de string pra buscar os funcionários
    por setor de uma empresa, e retorna qual(ais) é(são) o(os) funcionário(os)'''
    res=[]
    
    for linha in matriz:
       
        if linha[2] == setor:
            linha.pop(2)
            res.append(linha)
            
    return res