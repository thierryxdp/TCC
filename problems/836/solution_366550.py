def busca(setor, matriz):
        '''
        Busca cadastros de funcionários de acordo 
        com o setor;
        string, list -> list
        '''
        
        indices = [indice for indice, valor in enumerate(matriz[:][2]) if valor == setor]
        resultado = []
        for indice in indices:
            resultado.append(matriz[indice])
        return resultado