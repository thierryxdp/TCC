def busca(setor, matriz):
        '''
        Busca cadastros de funcionários de acordo 
        com o setor;
        string, list -> list
        '''
        
        indices = [indice for indice, valor in enumerate([linha[2] for linha in matriz]) if valor == setor]
        resultado = []
        for indice in indices:
            resultado.append(matriz[indice])
        return resultado