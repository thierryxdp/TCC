def passaColchao(dimensoesColchao, alturaPorta, larguraPorta):
        '''
        Para que o colchao passe, ele precisa ter duas dimensoes
        menor que a maior dimessao da porta
        '''
        maiorDimensaoDaPorta = max(alturaPorta, larguraPorta)
        list.insert(dimensoesColchao, 0, maiorDimensaoDaPorta)
        list.sort(dimensoesColchao)
        list.reverse(dimensoesColchao)
        posicao = list.index(dimensoesColchao, maiorDimensaoDaPorta)
        if (len(dimensoesColchao[:posicao]) <= 1):
            return True
        return False