def busca(setor, matriz):
        '''Função que recebe dados de uma empresa(nome,registro,setor,telefone), e uma entrada
        representando o setor a ser buscado e retorna uma Matriz com os dados buscados;
        str => list'''
        
        dados = []
        
        for i in range(len(matriz):
                if setor in matriz[i]:
                    dados.append(matriz[i])
        for e in range(len(dados)):
                       if dados[e][2] == setor:
                           del dados[e][2]