# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas_colchao,altura_porta,largura_porta):
    '''funcao retorna se o colchao passa ou nao na porta. list,float,float->bool'''
    if medidas_colchao[0]<altura_porta and medidas_colchao[1]<largura_porta or medidas_colchao[2]<largura_porta:
        return True
    elif medidas_colchao[0]<altura_porta and medidas_colchao[1]<largura_porta or medidas_colchao[2]<largura_porta:
        return True
    elif medidas_colchao[1]<altura_porta and medidas_colchao[0]<largura_porta or medidas_colchao[2]<largura_porta:
        return True
    elif medidas_colchao[1]<altura_porta and medidas_colchao[0]<largura_porta or medidas_colchao[2]<largura_porta:
        return True
    elif medidas_colchao[2]<altura_porta and medidas_colchao[0]<largura_porta or medidas_colchao[1]<largura_porta:
        return True
    elif medidas_colchao[2]<altura_porta and medidas_colchao[0]<largura_porta or medidas_colchao[1]<largura_porta:
        return True
    else:
        return False