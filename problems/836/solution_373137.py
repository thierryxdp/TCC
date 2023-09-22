def busca(setor, matriz):
    
    ''' Função que, fornecidos o setor desejado e 
        uma matriz com os dados dos funcionários de 
        uma empresa, retorna apenas os dados dos
        funcionários do setor informado.
        str, list -> list '''
    
    dados = []
    
    for linha in matriz:
        if linha[2] == setor:
            dados.append([linha[0], linha[1], linha[3]])
            
    return dados