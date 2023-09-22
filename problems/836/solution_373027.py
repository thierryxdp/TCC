def busca(setor, matriz):
    '''Fazer uma funcao que receba uma matriz e faca uma busca por setor, dado o nome dele e retorne os dados dos funcionarios daquele setor;
    string, list -> list'''
    
    resultado = []
    
    for lista in matriz:
        for coluna in lista:
            if coluna == setor:
                indice = list.index(lista,coluna)
                del lista[indice]
                resultado = resultado + [lista]
                
    return resultado