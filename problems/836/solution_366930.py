def busca(setor:str, matriz:list)->list:
    """Dada uma matriz com as informações de cada funcionário por linha e 
       com colunas sendo respectivamente nome, registro, setor e telefone
       a função filtra a matriz no setor inserido
       
       Parameters:
       matriz: matriz com 4 colunas(nome, registro, setor e telefone) e
       linhas são por funcionário então pode variar
       
       Returns:
       lista com informaçãoes dos funcionário de determinado setor
    """
    nlin = len(matriz)
    filtrados = []
    
    for funcionario in range(nlin):
        if setor == matriz[funcionario][2]:
            informacoes = matriz[funcionario]
            list.remove(informacoes,setor)
            list.append(filtrados,informacoes)
    return filtrados