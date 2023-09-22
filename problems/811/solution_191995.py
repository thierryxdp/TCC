# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas_colchao,alturaH,larguraL):
    """ função que dadas as medidas da colchao, altura e largura da porta, retorna;
        se o colchao consegue passar pela porta;
                 list,int,int-> bool"""
    resultado=bool
    
    if medidas_colchao [0] <=larguraL and medidas_colchao[1]<= alturaH:
        resultado= True
    elif medidas_colchao [1] <=larguraL and medidas_colchao[0]<= alturaH:
        resultado=True
    elif medidas_colchao [0] <=larguraL and medidas_colchao[2]<= alturaH:
        resultado= True
    else:
        resultado =False