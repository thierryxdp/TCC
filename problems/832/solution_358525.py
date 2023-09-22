def eh_quadrada(matriz):
        '''Função que verifica se uma matriz é quadrada.
        list->bool'''
        if range(len(matriz))==range(len(matriz[0])):
            return True

        else:
            return False