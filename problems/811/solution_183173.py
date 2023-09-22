def colchao(dimensoes,altura_porta, largura_porta):
    """função que recebe as dimensoes de um colchao e de uma porta e retoma True se o colchao passa na porta ou False se o colchao não passar na porta"""
    altura_colchao=dimensoes[0]
    largura_colchao=dimensoes[1]
    profundidade_colchao=dimensoes[2]
    if (largura_colchao <= altura_porta and altura_colchao <= largura_porta) or (altura_colchao <= altura_porta and largura_colchao <= largura_porta) or (largura_colchao <= altura_porta and profundidade_colchao <= largura_porta) or (profundidade_colchao <= altura_porta and largura_colchao <= largura_porta) or (altura_colchao <= altura_porta and profundidade_colchao <= largura_porta) or (profundidade_colchao <= altura_porta and altura_colchao <= largura_porta): 
       return True 
    else: 
        return False