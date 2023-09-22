def busca(string,matriz):
    '''Função faz uma busca por setor de uma dada empresa e retorna os funcionários desse setor;
    	str, list -> list'''

    lista= []
    
    for linhas in matriz:
        if linhas[2].lower() == string.lower():  #Usei o lower() para não diferenciar maiúscula de minúscula
            lista.append(linhas)
    return lista