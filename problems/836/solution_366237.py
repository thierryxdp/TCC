def busca(string,matriz):
    '''Função faz uma busca por setor de uma dada empresa e retorna os funcionários desse setor;
    	str, list -> list'''

    lista= []
    
    for linhas in matriz:
        if linhas[2] == string: 
            lista.append(linhas)
    return lista